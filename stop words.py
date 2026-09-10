import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('stopwords')
nltk.download('punkt_tab')  # Use 'punkt' if you're using an older NLTK version

# Load stop words
stop_words = set(stopwords.words("english"))
print(stop_words)

example_text = "Welcome to Scsvmv University. This is located in Kanchipuram. This is Tamil Nadu."

# Tokenize the text
words = word_tokenize(example_text)

# Remove stop words
filtered_sentence = []

for w in words:
    if w.lower() not in stop_words:   # Convert to lowercase for better filtering
        filtered_sentence.append(w)

print(filtered_sentence)
