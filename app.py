import requests
import json

url= "http://localhost:11434/api/chat"

payload={
    "model": "mistral",
    "message": [{
        "role":"user",
        "content":"What is Python"
        }]
}

response=requests.post(url, json=payload,stream=True)

if response.status_code==200:
    print("Streaming response from Ollama:")
    for line in response.iter_lines(decode_unicede=True):
        if line:
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["messafe"]["content"],end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()
else:
    pass