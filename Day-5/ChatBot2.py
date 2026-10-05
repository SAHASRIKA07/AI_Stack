import ollama
import streamlit as st
msgs = [
    {
        "role": "system",
        "content": "Give the answers in simple terms."
    }
]
while True:
    question = input("You:")
    if question.lower() == "exit":
        break
    msgs.append()