from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

example_text = ["finish", "finished", "finishes", "finishing"]

for w in example_text:
    print(ps.stem(w))

new_text = "It is very important to be pythonically while you are pythoning with python. All pythoners are mostly pythonsed at least once"

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
