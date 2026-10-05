import ollama 
while True:
    question = input("Ask the question:")
    if question.lower() == "exit":
        break
    response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role":"system",
            "content":"Give answers in 2 lines only "
        },
        {
            "role":"user",
            "content": question
        }
    ]
    )
    print (response["message"]["content"])
    #our simple bot does not have any memory, so it will not remember the previous questions and answers.