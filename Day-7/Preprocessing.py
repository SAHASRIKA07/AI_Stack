from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer('all-MiniLM-L6-v2')
with open("AISample.text","r") as file:
    text = file.read()
#print(text)
#text = file.readlines(),file.readline()
#print("No.of characters :",len(text))
chunks = []
chunk_size = 25
chunk_overlap = 10
step = chunk_size - chunk_overlap
for i in range(0,len(text),step):
    chunk = text[i : i+chunk_size] #(0,265,10) 
    chunks.append(chunk) #text[10:20]
#print("No.of chunks :",len(chunks))
#for i in range(0,len(chunks)):
 #   print("chunk -" ,i,":",chunks[i])
    #print(f"Chunk{i}->{chunks[i]}")
#Embeddings
embeddings = model.encode(chunks)
#print("Embeddings created Successfully")
#print("No.of embeddings :",len(embeddings))
#print(embeddings[0])
#print("shape of embeddings:",embeddings.shape)
#Chromadb 
client = chromadb.Client()
collection = client.create_collection(name = "My_documents")
print("Collection created successfully")
ids = []
for i in range(0,len(chunks)):
    ids.append(str(i))
collection.add(
    ids = ids,
    documents = chunks,
    embeddings = embeddings.tolist()
)
print("No.of collections :",collection.count())
results = collection.get()
for i in range(len(results['ids'])):
    print(f"ID : {results['ids'][i]} -> Chunk: {results['documents'][i]}")
chunk1 = collection.get(ids = ["0"])
print("Chunk 1:", chunk1)