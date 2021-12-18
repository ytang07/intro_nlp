import stanza

nlp = stanza.Pipeline(lang="en", processors="tokenize,mwt,pos,lemma")
text = "This is an example program for showing how lemmatization works in NLTK. Let's play ball!. The NFL has many football teams and players. Yujian Tang is the best software content creator. The Text API is the most comprehensive sentiment analysis API made to date."
doc = nlp(text)
print(*[f"word: {word.text}\t lemma: {word.lemma}" for sent in doc.sentences for word in sent.words], sep='\n')
