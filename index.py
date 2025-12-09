from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in depth analysis",
        config=types.GenerateContentConfig(
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        max_output_tokens=1024
    )
)
print(response.text)