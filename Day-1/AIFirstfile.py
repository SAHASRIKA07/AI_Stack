import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role":"user",
            "content":"Main types of AI models"
        }
    ]
)
print (response["message"]["content"])