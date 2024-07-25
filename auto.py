import openai
openai.api_key = 'sk-proj-WrSnsDkNSScySeBF4wooT3BlbkFJI1v7JtfYOalhUJLhu7mB'
messages = [{"role" : "system",
"content" :
           
           "You are a intelligent assistant."}]
while True:
    message = input("user : ")
    if message:
        messages.append(
            {"role" : "user",
            "content" : message},
        )
        chat = openai.Chatcompletion.create(
            model="gpt 4o ",
            message = messages
        ) 
        reply = chat.choices[0]message.content
        print(f"Chatgpt: {reply}")
        messages.append({"role":
        "assistant" , "content": reply})


