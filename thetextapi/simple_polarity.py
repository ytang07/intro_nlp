import requests
import json
from config import apikey

text = "The Text API is super easy to use and super useful for anyone who needs to do text processing. It's the best Text Processing web API and allows you to do amazing NLP without having to download or manage any models."
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
body = {
    "text": text
}
url = "https://app.thetextapi.com/text/text_polarity"

response = requests.post(url, headers=headers, json=body)
polarity = json.loads(response.text)["text polarity"]
print(polarity)