import ollama
# print(ollama.list())

response = ollama.chat(
    model="llama3.2-sm", 
    messages=[
        {"role": "user", "content": "Why is the sky blue?"},
    ])
print(response['message']['content'])
