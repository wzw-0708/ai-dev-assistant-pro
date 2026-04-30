from openai import OpenAI

client = OpenAI()

def ask_gpt(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5.3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content
