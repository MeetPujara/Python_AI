from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Can you tell what things are written in this img?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://imgs.search.brave.com/vB_DxFH5KBnCiZtMJwAttBx5Iop8teyyQq_lHaCM2ko/rs:fit:0:180:1:0/g:ce/aHR0cHM6Ly93d3cu/aW1nb2NyLmNvbS9i/bG9nLXVwbG9hZHMv/dGh1bWIvNS1jcmVh/dGl2ZS1pbWFnZS10/by10ZXh0LWNvbnZl/cnNpb24td2F5cy1p/bi1ldmVyeWRheS1s/aWZlLTE3MTk5OTM3/NzYud2VicA"
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)