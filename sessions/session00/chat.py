from anthropic import Anthropic

client = Anthropic()  # <— reads ANTHROPIC_API_KEY from environment

user_prompt = input("What is your question? ")

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    system="",
    messages=[
        {"role": "user", "content": user_prompt}
    ]
)

print(response.content[0].text)