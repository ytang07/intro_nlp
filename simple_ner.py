import requests
import json
from config import apikey

text = "Molly Moon is a cow. She is part of the United Nations' Climate Action Committee."
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
body = {
    "text": text
}
url = "https://app.thetextapi.com/text/ner"

response = requests.post(url, headers=headers, json=body)
ner = json.loads(response.text)["ner"]
print(ner)