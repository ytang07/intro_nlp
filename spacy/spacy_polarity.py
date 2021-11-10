import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')
text = "The Text API is super easy to use and super useful for anyone who needs to do text processing. It's the best Text Processing web API and allows you to do amazing NLP without having to download or manage any models."
doc = nlp(text)

print(doc._.polarity)