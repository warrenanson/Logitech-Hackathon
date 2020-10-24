import numpy
import nltk
from sys import stdin
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
#nltk.downloader.download('vader_lexicon')

sia = SIA()
results = []

print("Demo start!")

while True:
 
    word = input()

    pol_score = sia.polarity_scores(word)
    pol_score['Word'] = word
    results.append(pol_score)
    print(pol_score)

    if(pol_score['neg']>0.37):
        print('[Warning] Your words are offensive! Stop abusing!\n')