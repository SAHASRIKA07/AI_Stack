import ollama 
import streamlit as st 
st.title(":red[**Welcome to my ChatBot App...❕**]")
st.write("*👉Make your work easy. 💬Think bigger using AI Brain*")
with st.sidebar:
    st.header(":blue[⚙️Chat settings]")
    if st.button("🕳️Clear chat"):
        st.session_state.messages = []
        st.success("🗑️Chat history cleared!")
    personalities = {
        "👼Kid": "Answer the questions like you are explaining to a 5 year old child. Give me the answers only in 2 lines.",
        "🧑‍🤝‍🧑Friend": "Answer the questions in a friendly and casual manner. Give me the answers only in 2 lines.",
        "👩‍🏫Teacher": "Answer the questions in a professional and educational manner. Give me the answers only in 2 lines.",
        "🧙‍♂️Wizard": "Answer the questions like you are a wizard with magical knowledge. Give me the answers only in 2 lines.",
        "🩺Doctor": "Answer the questions like you are a doctor with medical knowledge. Give me the answers only in 2 lines.",
        "🕵️‍♂️Detective": "Answer the questions like you are a detective with investigative skills. Give me the answers only in 2 lines.",
        "🧑‍🚀Astronaut": "Answer the questions like you are an astronaut with space knowledge. Give me the answers only in 2 lines.",
        "🧑‍🍳Chef": "Answer the questions like you are a chef with culinary knowledge. Give me the answers only in 2 lines.",
        "🧑‍🎨Artist": "Answer the questions like you are an artist with creative knowledge. Give me the answers only in 2 lines.",
        "🧑‍💻Programmer": "Answer the questions like you are a programmer with coding knowledge. Give me the answers only in 2 lines.",
        "🧑‍🔬Scientist": "Answer the questions like you are a scientist with research knowledge. Give me the answers only in 2 lines.",
        "🧑‍⚖️Lawyer": "Answer the questions like you are a lawyer with legal knowledge. Give me the answers only in 2 lines.",
        "🤖robot": "Answer the questions like you are a robot with logical knowledge. Give me the answers only in 2 lines.",
    }
    personality = st.selectbox("🗝️Select a personality", personalities.keys())
    uploaded_file = st.file_uploader("🗂️Upload a text file....")
    try:
        if uploaded_file:
            context = uploaded_file.read().decode("utf-8")
            st.success("👍File uploaded successfully!")
            if st.button("Display"):
                st.write(context)
    except:
        pass 
        st.error("👎Error occurred while reading the file.")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
            {"role" : "user",
            "content" : question})
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("⏳Thinking..."):
        response = ollama.chat(
            model = "llama3.2:3b",
            messages = [
                {"role":"system","content":personalities[personality]}]
                + st.session_state.messages)
    st.session_state.messages.append(
            {"role":"assistant",
            "content":response["message"]["content"]
            }
        )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])
