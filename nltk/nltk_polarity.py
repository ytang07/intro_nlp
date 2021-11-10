# nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
text = "The Text API is super easy to use and super useful for anyone who needs to do text processing. It's the best Text Processing web API and allows you to do amazing NLP without having to download or manage any models."
scores = sia.polarity_scores(text)
print(scores)
