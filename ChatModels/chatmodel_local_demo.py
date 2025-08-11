import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={
        "max_length": 50,
        "temperature": 0.7,
        "top_p": 0.9
    }
)

result = llm.invoke("Write a short poem about the Internet.")
print(result)