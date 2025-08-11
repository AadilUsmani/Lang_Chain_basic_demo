from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np
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
doc=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
query = 'who is the greatest sportsman'
doc_vector = embedding_model.embed_documents(doc) # for doc embedding
query_vector = embedding_model.embed_query(query) # for query embedding

similarities = cosine_similarity([query_vector], doc_vector)[0]

index, score = sorted(list(enumerate(similarities)),key=lambda x:x[1])[-1]

print(query)
print(doc[index])
print("similarity score is:", score)  