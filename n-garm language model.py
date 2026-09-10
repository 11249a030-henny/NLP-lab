import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# Download tokenizer (run only once)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")

# Tokenize the sentence
tokens = word_tokenize(text)

print("\nOriginal Tokens")
print(tokens)

print("\nUnigrams")
for gram in ngrams(tokens, 1):
    print(gram)

print("\nBigrams")
for gram in ngrams(tokens, 2):
    print(gram)

print("\nTrigrams")
for gram in ngrams(tokens, 3):
    print(gram)
