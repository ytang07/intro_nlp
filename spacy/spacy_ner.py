import spacy

nlp = spacy.load("en_core_web_sm")

text = "Molly Moon is a cow. She is part of the United Nations' Climate Action Committee."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)