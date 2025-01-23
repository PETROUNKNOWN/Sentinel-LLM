import ollama

client=ollama.Client()

model="sentinel"
prompt="What is Python?"

response=client.generate(model=model,prompt=prompt)

print(f"Response froma Ollama model: {model}")
print(response.response)