import ollama
import streamlit as st

st.title("Image describer")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_bytes = uploaded_file.read()

print(uploaded_file)
if uploaded_file is not None:
    print(uploaded_file.name)
    print(type(uploaded_file.name))
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    response = ollama.chat(
        model="llava:7b",
        messages=[
            {
                "role": "user", 
                "content": "Describe the image.", 
                "images": [image_bytes]
            }])
    st.write(response['message']['content'])