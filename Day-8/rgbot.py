from sentence_transformers import SentenceTransformer
import chromadb
import ollama
import streamlit as st
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")
model = load_model()
st.snow()
st.title("Welcome to Ragbot !!!....")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Personalities
personalities = {
    "👼Kid": "Answer the questions like you are explaining to a 5 year old child. Give me the answers only in 2 lines.",
    "🧑‍🤝‍🧑Friend": "Answer the questions in a friendly and casual manner. Give me the answers only in 2 lines.",
    "👩‍🏫Teacher": "Answer the questions in a professional and educational manner. Give me the answers only in 2 lines."
}
with st.sidebar:
    st.header(":blue[⚙️Chat settings]")
    if st.button("🕳️Clear chat"):
        st.session_state.messages = []
        st.success("🗑️Chat history cleared!")
    personality = st.selectbox(
        "🗝️Select a personality",
        personalities.keys()
    )
    uploaded_file = st.file_uploader("Upload a file.")
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
        with st.expander("Preview"):
            st.text(text)
        chunks = []
        chunk_size = 100
        chunk_overlap = 20
        step = chunk_size - chunk_overlap
        for i in range(0, len(text), step):
            chunk = text[i:i + chunk_size]
            chunks.append(chunk)
        embeddings = model.encode(chunks)

        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_or_create_collection(
            name="My_documents"
        )
        ids = []
        for i in range(len(chunks)):
            ids.append(f"{uploaded_file.name}_{i}")

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist()
        )
question = st.chat_input("Ask a question...")
if question:
    if uploaded_file:
        with st.chat_message("user"):
            st.write(question)
        question_embedding = model.encode(question)
        results = collection.query(
            query_embeddings=[question_embedding.tolist()],
            n_results=3
        )
        retrieved_results = results["documents"][0]
        retrieved_ids = results["ids"][0]
        context = "\n".join(retrieved_results)
        prompt = f"""
        Answer the question using the context provided below.
        Question: {question}
        Context: {context}
        Answer:
        """
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        with st.chat_message("assistant"):
            st.write(response["message"]["content"])
        with st.expander("Source"):
            for i in range(3):
                st.warning(
                    f"Chunk {i+1}\n\n"
                    f"ID: {retrieved_ids[i]}\n\n"
                    f"Content: {retrieved_results[i]}"
                )
    else:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )
        with st.chat_message("user"):
            st.write(question)
        with st.spinner("⏳Thinking..."):
            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "system",
                        "content": personalities[personality]
                    }
                ] + st.session_state.messages
            )
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response["message"]["content"]
            }
        )
        with st.chat_message("assistant"):
            st.write(response["message"]["content"])