from sudorouter.httpx import TeeClient

client = TeeClient()
response = client.post(
    url="https://tee.sudorouter.ai/v1/chat/completions",
    headers={"Authorization": "Bearer <YourToken>"},
    json={
        "messages": [{"content": [{"type": "text", "text": "<Your prompt>"}], "role": "user"}],
        "model": "DeepSeek-R1-Distill-Llama-70B",
        "temperature": 0.7,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stream": True,
    },
)
print(response.text)
