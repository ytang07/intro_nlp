import stanza

nlp = stanza.Pipeline(lang='en', processors="tokenize,ner")

text = "Molly Moon is a cow. She is part of the United Nations' Climate Action Committee."
doc = nlp(text)

print(*[f"entity: {ent.text}\ttype: {ent.type}" for sent in doc.sentences for ent in sent.ents], sep='\n')