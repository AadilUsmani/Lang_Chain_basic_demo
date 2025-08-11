

# Run text generation locally using transformers
from transformers import pipeline

# Download and load the model (gpt2 is small and works on CPU)
generator = pipeline("text-generation", model="gpt2")

# Generate text
prompt = "Write a short poem about the Internet."
result = generator(prompt, max_length=50, num_return_sequences=1)
print(result[0]["generated_text"])