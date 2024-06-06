# Import the required libraries
import os
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st
from phi.assistant import Assistant
from phi.llm.gemini import Gemini
from phi.llm.groq import Groq
# from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from langchain_nvidia_ai_endpoints import ChatNVIDIA

import google.generativeai as genai


dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"), transport='rest')


# Set up the Streamlit app
st.title("AI Investment Agent 📈🤖")
st.caption("This app allows you to compare the performance of two stocks and generate detailed reports.")


# Create an instance of the Assistant
# assistant = Assistant(
#     llm=llm,
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
#     show_tool_calls=True,
#     )

# assistant = Assistant(
#     llm=Gemini(model="gemini-1.5-pro-latest"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
#     show_tool_calls=True,
#     # description="You help people with their health and fitness goals.",
# )

assistant = Assistant(
    name="Finance Assistant",
    llm=Groq(model="llama3-70b-8192"), #llm=Gemini(model="gemini-1.0-pro-latest"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=False,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    
)

# Input fields for the stocks to compare
stock1 = st.text_input("Enter the first stock symbol")
stock2 = st.text_input("Enter the second stock symbol")

if stock1 and stock2:
    # Get the response from the assistant
    query = f"Compare {stock1} to {stock2}. Use every tool you have."
    response = assistant.run(query, stream=False) #stream=False
    # response = assistant.print_response(query, markdown=False)
    # print(dir(response))
    # st.write(response)
    st.markdown(response)
    # st.markdown(assistant.print_response(query, markdown=True))
