#1. Generate a paragraph using Geminin llm ,
#  Task :
# i) Read a topic (string ) from a  variable or input . 
# ii) use the geminin model to generate a simple paragraph about the topic .
# iii) print the generate s parapgraph to the console . 
# ...existing code...
GEMENNI_API_KEY = "AIzaSyCEIoLn1A3369ATYNHjRFPGKmhlEU1fdUY"
import requests
import json

# Read topic from user input
topic = input("Enter a topic: ")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
headers = {
    'Content-Type': 'application/json',
    'X-goog-api-key': GEMENNI_API_KEY   
}
data = {
    "contents": [
        {
            "parts": [
                {"text": f"Write a simple paragraph about: {topic}"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

# Print only the generated paragraph
try:
    paragraph = result['candidates'][0]['content']['parts'][0]['text']
    print("\nGenerated Paragraph:\n", paragraph)
except (KeyError, IndexError):
    print("Failed to generate paragraph. Response :", result) 

