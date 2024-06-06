import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


client = OpenAI(
  base_url = "https://api.groq.com/openai/v1", #"https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("GROQ_API_KEY"), #api_key = os.getenv("NVIDIA_API_KEY")
)

completion = client.chat.completions.create(
  model="llama3-8b-8192",
  messages=[{"role":"user","content":"Give me a meal plan for today"}],
  temperature=0.5,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")