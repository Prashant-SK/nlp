import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from textatistic import Textatistic
import json
import string
import re

data = "BREAKING: All work and NO play makes JaCK dull boy. All work and no play makes jack a dull boy!?"
s = Textatistic(data)
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)

wordsFiltered = []
stopWordsInText = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
    else:
        stopWordsInText.append(w)

percentStopwords = (len(stopWordsInText) / len(wordsFiltered)) * 100

text = word_tokenize(data)
tagged = nltk.pos_tag(text)

counts = Counter(tag for word,tag in tagged)
nounCount = counts['NN']
verbCounts = Counter(tag for word,tag in tagged if tag == 'VBP' or tag == 'VB' or tag == 'VBZ' or tag == 'VBN' or tag == 'VBD')
wordLengths = [len(x) for x in data.split()]
avgWordLen = sum(wordLengths) / len(wordLengths)
numCapitalLetters = len(list(filter(lambda x: x in string.ascii_uppercase, data)))
CHARS = "!?"
shadyCharCount = len([char for char in data if char in CHARS])
capitalisedWords = re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",data)
print(capitalisedWords)
# print [word for word in data if for x.isUpper() in word]
print ("percent stopwords: ", percentStopwords)
print("average wordlength: ", avgWordLen)
print("No. of verbs: ",sum(verbCounts.values()))
print("FKE Readability: ", s.flesch_score)
print ("No. of nouns: ", nounCount)
print("Tokens: ", counts)
print("No. of Capital letters: ", numCapitalLetters)
print("No. of Shady Punctuation: ", shadyCharCount)
