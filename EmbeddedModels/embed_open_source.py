import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables from .env
load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
docs = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial Intelligence is transforming the world.",
    "LangChain is a framework for building applications with LLMs."
]
vectors = embedding_model.embed_documents(docs)
print(f"Number of embeddings: {len(vectors)}")
print(f"Embedding vector length: {len(vectors[0])}")
print(f"First 5 dimensions of first vector: {vectors[0][:5]}")