import asyncio
import json
import os
import sys
from contextlib import AsyncExitStack
from typing import Optional

from mcp import StdioServerParameters, stdio_client, ClientSession
from openai import AsyncOpenAI

# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import RotatingFileHandler


class StdioClientLogger:
    logger: logging.Logger | None = None

    @classmethod
    def setup_logger(cls):
        StdioClientLogger.logger = logging.getLogger("stdioclient")
        StdioClientLogger.logger.setLevel(logging.INFO)

        # 防止重复添加处理器
        if StdioClientLogger.logger.handlers:
            return

        log_file = os.path.expanduser("~") + "/logs/stdioclient/stdioclient.log"
        log_dir = os.path.dirname(log_file)
        os.makedirs(log_dir, exist_ok=True)

        formatter = logging.Formatter(
            "%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # 只添加文件处理器
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,  # 保留5个备份文件
            encoding="utf-8"
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        StdioClientLogger.logger.addHandler(file_handler)

        # 关键修复：防止日志向父logger传播
        StdioClientLogger.logger.propagate = False

    @classmethod
    def get_logger(cls) -> logging.Logger:
        if StdioClientLogger.logger is None:
            StdioClientLogger.setup_logger()
        if StdioClientLogger.logger is None:
            return logging.getLogger("stdioclient")
        else:
            return StdioClientLogger.logger

stdioclient_logger = StdioClientLogger.get_logger()

#集成LLM的目的：实现通过自然语言与计算器服务器进行交互的能力。
class MCPClient:
    def __init__(self):
        self.write = None
        self.stdio = None
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.AIHUBMIX_APIKEY=os.getenv("AIHUBMIX_APIKEY", "")
        self.client = AsyncOpenAI(
            # base_url="https://openrouter.ai/api/v1",
            base_url="https://aihubmix.com/v1",
            # api_key=os.getenv("OPENROUTER_API_KEY"),
            api_key=self.AIHUBMIX_APIKEY
        ) #在创建 OpenAI 客户端时指定 OpenRouter 的 base_url 和 api_key

    async def connect_to_server(self):
        server_params = StdioServerParameters(
            command="uvx",
            args=["nacos-mcp-router@latest"],
            env={"NACOS_PASSWORD": "nacos",
                 "NACOS_NAMESPACE": "public",
                 "ACCESS_KEY_ID": "ThisIsMyCustomSecretKey0123456789",
                 "ACCESS_KEY_SECRET": "ThisIsMyCustomSecretKey01234567899",
                 "MODE": "router",
                 "TRANSPORT_TYPE": "stdio"}
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # 列出可用工具
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_query(self, query: str) -> str:
        """使用 LLM 和 MCP 服务器提供的工具处理查询"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
        } for tool in response.tools]

        # 初始化 LLM API 调用
        response = await self.client.chat.completions.create(
            # model="qwen/qwen-plus",  #以<provider>/<model> 的格式,指定目标模型
            # model="deepseek-chat",
            # model="qwen/qwen2.5-vl-72b-instruct:free", #虽免费，但不支持tool use （tool calling）
            # model="qwen/qwen-turbo", #不免费，但网速慢，不容充值
            model= "gpt-4o-mini",
            messages=messages,
            tools=available_tools
        )#Supported Models: You can find models that support tool calling
        # by filtering on openrouter.ai/models?supported_parameters=tools.
        stdioclient_logger.info(f"1:respone={response}, messages={messages}, tools={available_tools}")
        final_text = []
        message = response.choices[0].message
        final_text.append(message.content or "")

        # 处理响应并处理工具调用
        while message.tool_calls:
            # 处理每个工具调用
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                # 执行工具调用
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")

                # 将工具调用和结果添加到消息历史
                messages.append({
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": tool_call.id,
                            "type": "function",
                            "function": {
                                "name": tool_name,
                                "arguments": json.dumps(tool_args)
                            }
                        }
                    ]
                })
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result.content)
                })

            # 将工具调用的结果交给 LLM
            response = await self.client.chat.completions.create(
                # model="qwen/qwen-plus",
                # model="qwen/qwen2.5-vl-72b-instruct:free",
                # model="qwen/qwen-turbo",
                model="gpt-4o-mini",
                messages=messages,
                tools=available_tools
            )
            stdioclient_logger.info(f"2:respone={response}, messages={messages}, tools={available_tools}")
            message = response.choices[0].message
            if message.content:
                final_text.append(message.content)

        return "\n".join(final_text)

    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()
                if query.lower() == 'quit':
                    break
                response = await self.process_query(query)
                print("\n" + response)
            except Exception as e:
                print(f"\nError:: {str(e)}")

    async def cleanup(self):
        await self.exit_stack.aclose()


async def main():
    client = MCPClient()
    try:
        await client.connect_to_server()
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
# client = Client("main.py")
#
# async def call_tool(tool_name: str, *args) -> str:
#     """Call a tool by name with given arguments."""
#     result = await client.call_tool(tool_name, *args)
#     print(f"{tool_name}({', '.join(map(str, args))}) = {result}")
#
# async def run():
#     """Run the client and call tools."""
#
#     async with client:
#         tools = await client.list_tools()
#         print(f"Available tools: {', '.join(tool.name for tool in tools)}")
#
#         await call_tool("add", {"a": 5, "b": 3})
#         await call_tool("subtract", {"a": 10, "b": 4})
#         await call_tool("multiply", {"a": 2, "b": 6})
#         await call_tool("divide", {"a": 8, "b": 2})
#         await call_tool("power", {"base": 2, "exponent": 3})
#
# if __name__ == "__main__":
#     asyncio.run(run())