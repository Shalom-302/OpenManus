from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()

# import asyncio
# api_key = os.getenv("DEEPSEEK_API_KEY")
# llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))

# # Configure the browser to connect to your Chrome instance
# browser = Browser(
#     config=BrowserConfig(
#         # Specify the path to your Chrome executable
#         chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
#         # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
#         # For Linux, typically: '/usr/bin/google-chrome'
#     )
# )

# # Create the agent with your configured browser
# agent = Agent(
#     task="va sur: https://www.linkedin.com/feed/ et cherche 5 posts recents qui parle de browser_use AI",
#     llm=llm,
#     browser=browser,
# )

# async def main():
#     await agent.run()

#     input('Press Enter to close the browser...')
#     await browser.close()

# if __name__ == '__main__':
#     asyncio.run(main())
    
    
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()
import asyncio

api_key = os.getenv("DEEPSEEK_API_KEY")
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))


async def main():
    agent = Agent(
        task="Écris un script Python qui génère la suite de Fibonacci jusqu'au 10ᵉ terme et exécute-le dans le navigateur chromium.",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())