import numpy
import nltk
from sys import stdin
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
#nltk.downloader.download('vader_lexicon')

sia = SIA()
results = []
abuse = False


print("Demo start!")


with open('abuse word.txt','r') as f:
    for line in f.readlines():

        pol_score = sia.polarity_scores(line)
        pol_score['Word'] = line
        results.append(pol_score)
        print(pol_score)

        if pol_score['neg'] > 0.37:
            abuse = True

        #if(pol_score['neg']>0.37):
        #    print('[Warning] Your words are offensive! Stop abusing!\n')

if abuse:
    print("[Warning] You have been detected game abusing and will be banned from playing games for a week as punishment ")