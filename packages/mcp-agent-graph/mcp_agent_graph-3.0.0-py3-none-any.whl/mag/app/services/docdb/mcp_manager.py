import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from bson import ObjectId

logger = logging.getLogger(__name__)


class MCPManager:
    """MCP生成管理器 - 负责mcp_messages集合的rounds格式消息管理"""

    def __init__(self, db, mcp_messages_collection, conversation_manager):
        """初始化MCP生成管理器"""
        self.db = db
        self.mcp_messages_collection = mcp_messages_collection
        self.conversation_manager = conversation_manager

    async def create_mcp_generation_conversation(self, conversation_id: str, user_id: str = "default_user") -> bool:
        """创建新的MCP生成对话"""
        try:
            # 1. 在conversations集合中创建基本信息
            conversation_success = await self.conversation_manager.create_conversation(
                conversation_id=conversation_id,
                conversation_type="agent",  # MCP生成属于agent类型
                user_id=user_id,
                title="AI生成MCP新对话",
                tags=[]
            )

            if not conversation_success:
                return False

            # 2. 在mcp_messages集合中创建消息文档
            now = datetime.utcnow()
            messages_doc = {
                "_id": conversation_id,
                "conversation_id": conversation_id,
                "rounds": [],
                "parsed_results": {
                    "analysis": None,
                    "todo": None,
                    "folder_name": None,
                    "script_files": {},  # {"文件名.py": "文件内容"}
                    "dependencies": None,
                    "readme": None
                }
            }

            await self.mcp_messages_collection.insert_one(messages_doc)
            logger.info(f"创建MCP生成对话成功: {conversation_id}")
            return True

        except Exception as e:
            if "duplicate key" in str(e).lower():
                logger.warning(f"MCP生成对话已存在: {conversation_id}")
                return False
            logger.error(f"创建MCP生成对话失败: {str(e)}")
            return False

    async def get_mcp_generation_conversation(self, conversation_id: str) -> Optional[Dict[str, Any]]:
        """获取MCP生成对话（包含基本信息和详细消息）"""
        try:
            # 获取基本信息
            conversation_info = await self.conversation_manager.get_conversation(conversation_id)
            if not conversation_info or conversation_info.get("type") != "agent":
                return None

            # 获取详细消息
            messages_doc = await self.mcp_messages_collection.find_one({"conversation_id": conversation_id})
            if not messages_doc:
                return None

            # 合并返回
            result = conversation_info.copy()
            result.update({
                "rounds": messages_doc.get("rounds", []),
                "parsed_results": messages_doc.get("parsed_results", {})
            })

            # 将rounds转换为messages（如果需要）
            messages = []
            for round_data in messages_doc.get("rounds", []):
                messages.extend(round_data.get("messages", []))
            result["messages"] = messages

            return self._convert_objectid_to_str(result)
        except Exception as e:
            logger.error(f"获取MCP生成对话失败: {str(e)}")
            return None

    async def add_message_to_mcp_generation(self, conversation_id: str,
                                            message: Dict[str, Any],
                                            model_name: str = None) -> bool:
        """向MCP生成对话添加消息（自动管理rounds）"""
        try:
            # 获取当前rounds数量来确定是否需要创建新round
            messages_doc = await self.mcp_messages_collection.find_one(
                {"conversation_id": conversation_id},
                {"rounds": 1}
            )

            if not messages_doc:
                logger.error(f"MCP生成对话不存在: {conversation_id}")
                return False

            current_rounds = messages_doc.get("rounds", [])
            message_role = message.get("role")

            if message_role == "system":
                if not current_rounds:
                    # 创建第一个round，包含system消息
                    round_data = {
                        "round": 1,
                        "messages": [message]
                    }
                    result = await self.mcp_messages_collection.update_one(
                        {"conversation_id": conversation_id},
                        {"$push": {"rounds": round_data}}
                    )
                else:
                    # 添加到第一个round的开头
                    result = await self.mcp_messages_collection.update_one(
                        {"conversation_id": conversation_id},
                        {"$push": {"rounds.0.messages": {"$each": [message], "$position": 0}}}
                    )

            elif message_role == "user":
                # User消息处理逻辑
                if not current_rounds:
                    round_data = {
                        "round": 1,
                        "messages": [message]
                    }
                    result = await self.mcp_messages_collection.update_one(
                        {"conversation_id": conversation_id},
                        {"$push": {"rounds": round_data}}
                    )
                    # 更新round计数
                    await self.conversation_manager.update_conversation_round_count(conversation_id, 1)

                elif len(current_rounds) == 1:
                    first_round = current_rounds[0]
                    first_round_messages = first_round.get("messages", [])

                    # 检查第一个round是否已经有user消息
                    has_user_message = any(msg.get("role") == "user" for msg in first_round_messages)

                    if not has_user_message:
                        result = await self.mcp_messages_collection.update_one(
                            {"conversation_id": conversation_id},
                            {"$push": {"rounds.0.messages": message}}
                        )
                    else:
                        # 第一个round已经有user消息，创建新round
                        new_round_number = len(current_rounds) + 1
                        round_data = {
                            "round": new_round_number,
                            "messages": [message]
                        }
                        result = await self.mcp_messages_collection.update_one(
                            {"conversation_id": conversation_id},
                            {"$push": {"rounds": round_data}}
                        )
                        await self.conversation_manager.update_conversation_round_count(conversation_id, 1)
                else:
                    new_round_number = len(current_rounds) + 1
                    round_data = {
                        "round": new_round_number,
                        "messages": [message]
                    }
                    result = await self.mcp_messages_collection.update_one(
                        {"conversation_id": conversation_id},
                        {"$push": {"rounds": round_data}}
                    )
                    await self.conversation_manager.update_conversation_round_count(conversation_id, 1)

            else:
                # Assistant消息：总是添加到最后一个round
                if not current_rounds:
                    round_data = {
                        "round": 1,
                        "messages": [message]
                    }
                    result = await self.mcp_messages_collection.update_one(
                        {"conversation_id": conversation_id},
                        {"$push": {"rounds": round_data}}
                    )
                    await self.conversation_manager.update_conversation_round_count(conversation_id, 1)
                else:
                    # 添加到最后一个round
                    last_round_index = len(current_rounds) - 1
                    result = await self.mcp_messages_collection.update_one(
                        {"conversation_id": conversation_id},
                        {"$push": {f"rounds.{last_round_index}.messages": message}}
                    )

            if result.modified_count > 0:
                logger.info(f"向MCP生成对话 {conversation_id} 添加 {message_role} 消息成功")

                # 只在添加assistant消息时检查是否需要生成title和tags
                if message_role == "assistant":
                    await self._check_and_generate_title_tags(conversation_id, model_name)

                return True
            else:
                logger.error(f"向MCP生成对话 {conversation_id} 添加 {message_role} 消息失败")
                return False

        except Exception as e:
            logger.error(f"添加MCP生成对话消息失败: {str(e)}")
            return False

    async def _check_and_generate_title_tags(self, conversation_id: str, model_name: str = None):
        """检查并生成标题和标签（当标题为默认标题时）"""
        try:
            # 获取当前对话基本信息
            conversation_info = await self.conversation_manager.get_conversation(conversation_id)
            if not conversation_info:
                return

            current_title = conversation_info.get("title", "")

            # 只在标题为默认标题时生成新标题和标签
            if current_title == "AI生成MCP新对话":
                # 获取消息进行标题生成
                messages_doc = await self.mcp_messages_collection.find_one(
                    {"conversation_id": conversation_id},
                    {"rounds": 1}
                )

                if messages_doc and messages_doc.get("rounds"):
                    # 收集所有消息用于标题生成
                    all_messages = []
                    for round_data in messages_doc["rounds"]:
                        all_messages.extend(round_data.get("messages", []))

                    # 使用指定的模型或回退到第一个可用模型
                    model_config = None
                    if model_name:
                        from app.services.model_service import model_service
                        model_config = model_service.get_model(model_name)

                    if not model_config:
                        # 回退到第一个可用模型
                        from app.services.model_service import model_service
                        available_models = list(model_service.clients.keys())
                        if not available_models:
                            logger.warning("没有可用的模型进行标题生成")
                            return
                        model_config = model_service.get_model(available_models[0])

                    if not model_config:
                        return

                    # 调用统一的标题和标签生成方法
                    await self.conversation_manager.generate_conversation_title_and_tags(
                        conversation_id=conversation_id,
                        messages=all_messages,
                        model_config=model_config
                    )

                    logger.info(
                        f"为MCP生成对话 {conversation_id} 生成标题和标签，使用模型: {model_config.get('name', 'unknown')}")

        except Exception as e:
            logger.error(f"生成MCP生成对话标题和标签时出错: {str(e)}")

    async def update_mcp_generation_parsed_results(self, conversation_id: str,
                                                   parsed_results: Dict[str, Any]) -> bool:
        """更新MCP生成对话的解析结果 - 支持脚本文件的增删改"""
        try:
            update_operations = []

            # 处理简单替换字段（新增folder_name）
            simple_fields = ["analysis", "todo", "folder_name", "dependencies", "readme"]
            set_updates = {}

            for field in simple_fields:
                if field in parsed_results and parsed_results[field] is not None:
                    set_updates[f"parsed_results.{field}"] = parsed_results[field]

            # 处理脚本文件增删改逻辑
            if "script_files" in parsed_results and parsed_results["script_files"]:
                # 获取当前对话数据
                messages_doc = await self.mcp_messages_collection.find_one({"conversation_id": conversation_id})
                if messages_doc:
                    current_script_files = messages_doc.get("parsed_results", {}).get("script_files", {})

                    # 合并新的脚本文件（新文件会替换同名文件）
                    updated_script_files = current_script_files.copy()
                    updated_script_files.update(parsed_results["script_files"])

                    set_updates["parsed_results.script_files"] = updated_script_files

            # 处理脚本文件删除逻辑
            if "delete_script_files" in parsed_results and parsed_results["delete_script_files"]:
                messages_doc = await self.mcp_messages_collection.find_one({"conversation_id": conversation_id})
                if messages_doc:
                    current_script_files = messages_doc.get("parsed_results", {}).get("script_files", {})
                    updated_script_files = current_script_files.copy()

                    for file_name in parsed_results["delete_script_files"]:
                        if file_name in updated_script_files:
                            del updated_script_files[file_name]
                            logger.info(f"删除脚本文件: {file_name}")

                    set_updates["parsed_results.script_files"] = updated_script_files

            # 执行更新操作
            if set_updates:
                result = await self.mcp_messages_collection.update_one(
                    {"conversation_id": conversation_id},
                    {"$set": set_updates}
                )
                return result.modified_count > 0

            return True

        except Exception as e:
            logger.error(f"更新MCP生成解析结果失败: {str(e)}")
            return False

    async def update_mcp_generation_token_usage(self, conversation_id: str,
                                                prompt_tokens: int, completion_tokens: int) -> bool:
        """更新MCP生成对话的token使用量"""
        try:
            return await self.conversation_manager.update_conversation_token_usage(
                conversation_id, prompt_tokens, completion_tokens
            )
        except Exception as e:
            logger.error(f"更新MCP生成token使用量失败: {str(e)}")
            return False

    async def get_mcp_generation_messages_only(self, conversation_id: str) -> Optional[Dict[str, Any]]:
        """仅获取MCP生成的消息部分（不包含基本信息）"""
        try:
            messages_doc = await self.mcp_messages_collection.find_one({"conversation_id": conversation_id})
            if messages_doc:
                return self._convert_objectid_to_str(messages_doc)
            return None
        except Exception as e:
            logger.error(f"获取MCP生成消息失败: {str(e)}")
            return None

    async def delete_mcp_generation_messages(self, conversation_id: str) -> bool:
        """删除MCP生成消息"""
        try:
            result = await self.mcp_messages_collection.delete_one({"conversation_id": conversation_id})
            if result.deleted_count > 0:
                logger.info(f"MCP生成消息 {conversation_id} 已删除")
                return True
            else:
                logger.warning(f"MCP生成消息 {conversation_id} 不存在")
                return False
        except Exception as e:
            logger.error(f"删除MCP生成消息失败: {str(e)}")
            return False

    def _convert_objectid_to_str(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        """将ObjectId转换为字符串"""
        if isinstance(doc.get("_id"), ObjectId):
            doc["_id"] = str(doc["_id"])
        return doc