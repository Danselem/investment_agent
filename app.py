# Import the required libraries
import os
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st
from phi.assistant import Assistant
from phi.llm.groq import Groq
from phi.tools.yfinance import YFinanceTools


dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Set up the Streamlit app
st.title("AI Investment Agent 📈🤖")
st.caption("This app allows you to compare the performance of two stocks and generate detailed reports.")



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
    response = assistant.run(query, stream=False) 
    st.markdown(response)
