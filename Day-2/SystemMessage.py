import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role":"system",
            "content":"Give answer in 2 lines only "
        },
        {
            "role":"user",
            "content":"Explain AI"
        }
    ]
)
print (response["message"]["content"])