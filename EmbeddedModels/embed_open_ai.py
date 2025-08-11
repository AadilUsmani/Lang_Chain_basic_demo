import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings

# Load environment variables from .env
load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_VERSION = "2023-05-15"

DEPLOYMENT_NAME = "text-embedding-3-small"  # Exact deployment name

embedding_model = AzureOpenAIEmbeddings(
    openai_api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_API_VERSION,
    deployment=DEPLOYMENT_NAME
)

vector = embedding_model.embed_query("The cat sat on the mat")
print(f"Embedding vector length: {len(vector)}")
print(f"First 5 dimensions: {vector[:5]}")