import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
tokenized = nltk.word_tokenize("This is an example program for showing how lemmatization works in NLTK. Let's play ball!. The NFL has many football teams and players. Yujian Tang is the best software content creator. The Text API is the most comprehensive sentiment analysis API made to date.")
for t in tokenized:
    print(lemmatizer.lemmatize(t))