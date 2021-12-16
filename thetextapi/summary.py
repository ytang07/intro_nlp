import requests
import json

from config import apikey

text = "The Text API is easy to use and useful for anyone who needs to do text processing. It's the best Text Processing web API. The Text API allows you to do amazing NLP without having to download or manage any models. The Text API provides many NLP capabilities. These capabilities range from custom Named Entity Recognition (NER) to Summarization to extracting the Most Common Phrases. NER and Summarizations are both commonly used endpoints with business use cases. Use cases include identifying entities in articles, summarizing news articles, and more. The Text API is built on a transformer model."
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
body = {
    "text": text
}
url = "https://app.thetextapi.com/text/summarize"

response = requests.post(url, headers=headers, json=body)
summary = json.loads(response.text)["summary"]
print(summary)
