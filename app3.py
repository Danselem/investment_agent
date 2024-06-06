import os
from dotenv import load_dotenv
from pathlib import Path
from phi.assistant import Assistant
from phi.tools.yfinance import YFinanceTools
# from phi.llm.openai import OpenAIChat
from phi.llm.groq import Groq

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

assistant = Assistant(
    name="Finance Assistant",
    llm=Groq(model="mixtral-8x7b-32768"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
)

for i in dir(assistant):
    print(i)
# assistant.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)