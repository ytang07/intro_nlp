import nltk

text = "Molly Moon is a cow. She is part of the United Nations' Climate Action Committee."

tokenized = nltk.word_tokenize(text)
pos_tagged = nltk.pos_tag(tokenized)
chunks = nltk.ne_chunk(pos_tagged)
for chunk in chunks:
    if hasattr(chunk, 'label'):
        print(chunk)

print(nltk.help.upenn_tagset())