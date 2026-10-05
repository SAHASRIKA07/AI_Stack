from sentence_transformers import SentenceTransformer
import chromadb, ollama
model = SentenceTransformer("all-MiniLM-L6-v2")
file_name = "Sample.text"
with open("Sample.text","r")as file:
    text = file.read()
chunks = []
chunk_size = 100 
chunk_overlap = 20 
step = chunk_size - chunk_overlap
for i in range(0,len(text),step):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
embeddings = model.encode(chunks)
client = chromadb.PersistentClient(path = "./chroma_db")
collection = client.get_or_create_collection(name = "My_documents")
ids = []
for i in range(0,len(chunks)):
    ids.append(f"{file_name}_{i}")
collection.add(
    ids = ids,
    documents = chunks,
    embeddings = embeddings.tolist()
)
question = input("Ask a question...")
question_embedding = model.encode(question)
results = collection.query(
    query_embeddings = [question_embedding.tolist()],
    n_results= 3
)
retrieved_results = results['documents'][0]
retrieved_ids = results['ids'][0]
#for i in range(len(retrieved_results)):
#print(f"Chunk_{i}\n")
#print(results['documents'][0][i])
#Prompting
context = '\n'.join(retrieved_results)
#print(retrieved_results)
#print(context)
prompt = f'''
Answer the question using the context provided below.
Question : {question}
Context : {context}
Answer:
'''
#print(prompt)
response = ollama.chat(
    model= "llama3.2:3b",
    messages=[{"role":"user","content":prompt}]
)
print(response["message"]["content"])