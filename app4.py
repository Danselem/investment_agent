import os
from dotenv import load_dotenv
from pathlib import Path
from phi.assistant import Assistant
from phi.llm.gemini import Gemini
import google.generativeai as genai

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"), transport='rest')

assistant = Assistant(
    llm=Gemini(model="gemini-1.0-pro-latest"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response("Share a quick healthy breakfast recipe.", markdown=True)
