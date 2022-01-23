import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
 
def get_sentences(nlp:spacy.lang, text: str, keyword: str):
    words = keyword.split(" ")
    doc = nlp(text)
    pattern = []
    for word in words:
        pattern.append({"TEXT": word})
    matcher = Matcher(nlp.vocab)
    matcher.add(keyword, [pattern])
    retval = []
    for sent in doc.sents:
        for match_id, start, end in matcher(nlp(sent.text)):
            if nlp.vocab.strings[match_id] in [keyword]:
                snippet = sent.text
                retval.append(snippet)
    return list(set(retval))

text = """Green energy will be the backbone of decarbonizing our energy systems, and by extension, human society as a whole. Using the breakdown of GHG emissions by sector in the US below, replacing our direct electricity usage emissions with electricity from green energy sources (we can call this green electricity) would already reduce emissions by 25%. Furthermore, reducing emissions from transport and industry (another 52% of emissions) would require replacing burning hydrocarbons with using green electricity in a process called electrification. For transportation, replacing internal combustion engine vehicles with electric vehicles would enable the transportation sector to use green electricity instead of gasoline. For industry, electrifying manufacturing equipment or combining heat and power processes can enable the sector to use green electricity instead of burning coal. For commercial and residential, we could electrify heating and cooling for homes. Right now, there's a lot of propane and natural gas systems, and converting these to electricity would reduce the carbon footprint of the average American home. These pathways to decarbonization suggest that we need to install a lot of green electricity capacity and ensure our energy systems (like the electric grid) are capable of meeting people's new and existing demands without relying on hydrocarbons."""
kw = "energy"
print(get_sentences(nlp, text, kw))