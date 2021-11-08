import nltk
from nltk.tokenize import word_tokenize

text = """This is where the calculation can get tricky. Here’s the thing about solar energy. Solar energy comes from the sun. That means solar panels cannot produce energy 24 hours a day. They only produce energy during sunlight hours. That energy then has to be stored somewhere while it is not being used. Energy storage is a whole other topic in and of itself. Let me get back to the point, there’s only an average of 4 peak sunlight hours a day. A solar panel may get more than that, but let’s take a conservative estimate of our solar power generation and confine it to those 4 hours only. 
Back to the calculations. At 4 acres of solar panels to generate a megawatt-hour and 4 hours of power generation time a day, a 1 MW solar farm would generate 4 MWh of power over 4 acres every day. At 110,000 megawatt-hours of power needed a day to power America, we would need about 110,000 acres of solar farm. 110,000 acres? That sounds huge, that’s more land than the entire Mojave desert. It’s not as daunting as it sounds, there are 1.9 billion acres in the continental United States, and 110,000 acres is only slightly more than 0.5 percent of the total land of the continental US."""

tokenized = word_tokenize(text)
tagged = nltk.pos_tag(tokenized)
for tag in tagged:
    print(tag)