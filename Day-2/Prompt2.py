import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role":"user",
            "content":"Waht is AI in 2 lines , what are the 3 main types, give me the 2 examples of AI and explain the examples in 2 lines each "
        }
    ]
)
print (response["message"]["content"])