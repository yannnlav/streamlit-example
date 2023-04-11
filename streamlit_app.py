import streamlit as st
import openai
import os

openai.api_key = st.secrets["api_key"]

def ask_question(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

st.title("Welcome to the company FAQ chatbot!")
st.write("Below are some frequently asked questions with their corresponding answers generated by OpenAI.")
st.write("If you have another question, you can type it in the box below.")

# Define the FAQ questions and answers
faqs = [
    {"question": "What are the work hours?", "answer": ""},
    {"question": "What are the company policies regarding sick leave?", "answer": ""},
    {"question": "What is the dress code?", "answer": ""},
    {"question": "What are the benefits offered by the company?", "answer": ""},
    {"question": "Who do I contact if I have a question or concern?", "answer": ""},
    {"question": "How often do performance evaluations occur?", "answer": ""},
]

# Populate the FAQ answers using OpenAI
for faq in faqs:
    faq["answer"] = ask_question(faq["question"])

# Display the FAQ questions and answers
for faq in faqs:
    st.write(f"Q: {faq['question']}")
    st.write(f"A: {faq['answer']}")
    st.write("---")

# Allow the user to ask additional questions
while True:
    user_question = st.text_input("Ask another question:")
    if user_question:
        answer = ask_question(user_question)
        st.write(f"A: {answer}")
    if st.button("Quit"):
        st.write("Thank you for using the chatbot. Goodbye!")
        break
