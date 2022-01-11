import requests
import json
from config import apikey

headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
kw_url = "https://app.thetextapi.com/text/sentences_with_keywords"
text = """Green energy will be the backbone of decarbonizing our energy systems, and by extension, human society as a whole. Using the breakdown of GHG emissions by sector in the US below, replacing our direct electricity usage emissions with electricity from green energy sources (we can call this green electricity) would already reduce emissions by 25%. Furthermore, reducing emissions from transport and industry (another 52% of emissions) would require replacing burning hydrocarbons with using green electricity in a process called electrification. For transportation, replacing internal combustion engine vehicles with electric vehicles would enable the transportation sector to use green electricity instead of gasoline. For industry, electrifying manufacturing equipment or combining heat and power processes can enable the sector to use green electricity instead of burning coal. For commercial and residential, we could electrify heating and cooling for homes. Right now, there's a lot of propane and natural gas systems, and converting these to electricity would reduce the carbon footprint of the average American home. These pathways to decarbonization suggest that we need to install a lot of green electricity capacity and ensure our energy systems (like the electric grid) are capable of meeting people's new and existing demands without relying on hydrocarbons."""
kws = ["energy", "process"]
body = {
    "text": text,
    "keywords": kws
}

response = requests.post(kw_url, headers=headers, json=body)
_dict = json.loads(response.text)
print(_dict["energy"])
print(_dict["process"])
