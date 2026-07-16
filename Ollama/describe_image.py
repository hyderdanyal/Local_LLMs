import ollama
import os

print("Reached here")

print(os.getcwd())
print(os.path.exists("image.jpg"))

response = ollama.chat(
    model="llava:7b",
    messages=[
        {
            "role": "user", 
            "content": "Describe the image.", 
            "images": ['image.jpg']
        }])
print(response['message']['content'])