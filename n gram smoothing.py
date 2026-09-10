import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Download tokenizer (Run only once)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a text corpus: ").lower()

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation
tokens = [word for word in tokens if word.isalpha()]

# Count word frequencies
word_count = Counter(tokens)

# Vocabulary size
V = len(word_count)

# Total number of words
N = sum(word_count.values())

print("\nWord\t\tCount\tSmoothed Probability")
print("-" * 50)

for word in word_count:
    probability = (word_count[word] + 1) / (N + V)
    print(f"{word:15}{word_count[word]:5}\t{probability:.4f}")
