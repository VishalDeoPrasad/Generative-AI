from openai import OpenAI
import streamlit as st

f = open("keys\.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

###########################################################
st.snow()
st.title("An AI🤖 Code Reviewer")
############################################################

prompt = st.text_area("🧑‍💻Check You Python code here....")

if st.button("Generate") == True:
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
        {"role": "system", "content" : """
         "You are a AI Assistant and your task is to accept a Python code as input from the user and help them by identifing errors and fix error in the prompt. Your output has the following structure:
         you have to tell mistakes
         you have to write full correct code in prompt"
         
         """},
        {"role": "user", "content": prompt}
        ]
    )
    
    st.write(response.choices[0].message.content)