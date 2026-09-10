import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)

print(f"\n{'Word':<15}{'POS Tag'}")
print("-" * 25)

for word, tag in pos_tags:
    print(f"{word:<15}{tag}")
