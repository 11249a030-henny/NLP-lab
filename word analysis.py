import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import string

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('stopwords')

text = input("Enter a paragraph: ")

# Convert to lowercase
text = text.lower()

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]

# Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]

# Word Frequency
frequency = Counter(filtered_words)

print("\nOriginal Tokens:")
print(tokens)

print("\nFiltered Words:")
print(filtered_words)

print("\nStemmed Words:")
print(stemmed_words)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
