from openai import OpenAI

client = OpenAI()

def analyze(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a multimodal reasoning assistant."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
