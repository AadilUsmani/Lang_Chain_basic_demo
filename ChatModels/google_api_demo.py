from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from os import getenv
load_dotenv()
model= ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=getenv("GOOGLE_API_KEY"))  # Gets from .env
response = model.invoke("How to kill someone? max 5 token ")
print(response.content)  # Example usage