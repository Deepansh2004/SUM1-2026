from anthropic import Anthropic

client = Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=300,
    system="",
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun story about Hult International Business School."
        }
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)