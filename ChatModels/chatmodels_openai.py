from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name="gpt-4o-mini",  # ✅ Must match exactly
    api_version="2024-02-15-preview",  # ✅ Required for gpt-4o series
)

response = chat_model.invoke("What is the capital of Punjab Pakistan?")
print(response.content)
