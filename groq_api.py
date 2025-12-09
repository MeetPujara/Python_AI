from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
    ]

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye")
        break
    
    messages.append({
        "role": "user",
        "content": user_input
    })

    stream = client.chat.completions.create(
        messages=messages, 
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        max_completion_tokens=120,
        top_p=1,
        stream=False,
    )
    
    assistant_response = stream.choices[0].message.content
    print(f"Assistant: {assistant_response}")
    
    messages.append({
        "role": "assistant",
        "content": assistant_response
    })