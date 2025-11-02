### Summarise text file using LLM . 
## Task: Read a text file . 
## use an AI/LLM model to summarize the content of in 2 -3 sentences . 
## Write the summary output.txt file . 
## Write the summary to output.txt 

### Summarise the content in 2-3 sentences . 
### Summarise text file using LLM . 
## Task: Read a text file . 
## use an AI/LLM model to summarize the content of in 2 -3 sentences . 
## Write the summary output.txt file . 
GEMENNI_API_KEY = "AIzaSyCEIoLn1A3369ATYNHjRFPGKmhlEU1fdUY"
import requests
import json

# Read the content of the file
with open("input.txt", "r") as file:
    content = file.read()

# Prepare the prompt for the model
prompt = f"Summarize the following text in 2-3 sentences:\n{content}"

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
headers = {
    'Content-Type': 'application/json',
    'X-goog-api-key': GEMENNI_API_KEY
}
data = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

# Extract the summary and write to output.txt
try:
    summary = result['candidates'][0]['content']['parts'][0]['text']
    with open("output.txt", "w") as out_file:
        out_file.write(summary)
    print("Summary written to output.txt")
except (KeyError, IndexError):
    print("Failed to generate summary. Response:", result)