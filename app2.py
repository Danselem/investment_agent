import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai


dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"), transport='rest')

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

response = model.generate_content("Please provide a list of the most influential people in the world.")
print(response.text)