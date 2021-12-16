import spacy

nlp = spacy.load("en_core_web_sm")

text = "This is an example program for showing how lemmatization works in spaCy. Let's play ball!. The NFL has many football teams and players. Yujian Tang is the best software content creator. The Text API is the most comprehensive sentiment analysis API made to date."

doc = nlp(text)

for token in doc:
    print(token.lemma_)