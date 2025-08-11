from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

LLM = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),  # Gets from .env
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),          # Gets from .env
    api_version="2024-02-15-preview",
    deployment_name="gpt-4o-mini",
    max_tokens=15 
)


result=LLM.invoke("What is the capital of Palestine?Answer in 8 words maximum")  # Example usage

print(result.content)