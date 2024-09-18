import os
import openai
import asyncio
from dotenv import load_dotenv

load_dotenv()
# Define AzureOpenAI environment variables
client = openai.AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

print(os.getenv("AZURE_OPENAI_ENDPOINT"))
print(os.getenv("AZURE_OPENAI_API_KEY"))
print(os.getenv("AZURE_OPENAI_API_VERSION"))
print(os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"))

system_prompt = 'Eres un profesor de matemáticas que resuelve problemas.'
user_prompt = '¿Cuanto es 2+2?'
messages = [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]

try:
    completion = client.chat.completions.create(
                    model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
                    messages=messages,
                    top_p=0.9,
                    temperature=0.5
                )
    print(completion)
except Exception as e:
    print(f"An exception occurred: {e}")


