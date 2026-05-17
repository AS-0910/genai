from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
# from langchain.agents import create_agent
from langchain_core.tools import Tool

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm =init_chat_model("google_genai:gemini-3-flash-preview",api_key=api_key)

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathsserver.py"],
                "transport":"stdio"
            },

            "weather":{
                "url":"http://localhost:9001/mcp",
                "transport":"streamable-http",
            }
        }
    )

    tools = await client.get_tools()
    # print(type(tools), tools) 
    agent = create_react_agent(llm,tools)


    math_response = await agent.ainvoke(
        {"messages" : [{"role":"user","content":"What is 2 + 3?"}]}
    )

    weather_response = await agent.ainvoke(
        {"messages" : [{"role":"user","content":"What is the weather like today in California?"}]}
    )

    print("Math Response:", math_response['messages'][-1].content)
    print("Weather Response:", weather_response['messages'][-1].content)


asyncio.run(main())



