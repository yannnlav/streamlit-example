import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

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

st.title("Welcome to the company!")
st.write("Below are the frequently asked questions with their corresponding answers generated by OpenAI.")
st.write("If you wish to ask another question, you can type it in the text box below.")

# Print common questions and their answers
questions_and_answers = [
    ("What are the work hours?", ""),
    ("What are the company policies regarding sick leave?", ""),
    ("What is the dress code?", ""),
    ("What are the benefits offered by the company?", ""),
    ("Who do I contact if I have a question or concern?", ""),
    ("How often do performance evaluations occur?", "")
]

for question, _ in questions_and_answers:
    answer = ask_question(question)
    questions_and_answers[questions_and_answers.index((question, _))] = (question, answer)

# Create a dropdown menu for users to select a question
selected_question = st.selectbox(
    "Select a question:",
    [question for question, answer in questions_and_answers],
)

# Display the answer to the selected question
st.write(f"Q: {selected_question}")
st.write(f"A: {questions_and_answers[[question for question, answer in questions_and_answers].index(selected_question)][1]}")

# Allow the user to ask another question or quit the chatbot
while True:
    question = st.text_input("Enter another question or type 'quit' to exit:")
    if question == "quit":
        st.write("Exiting the program...\nThank you for using the chatbot. Good bye!")
        break
    else:
        answer = ask_question(question)
        st.write(f"A: {answer}")
