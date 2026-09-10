from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hey, welcome to SCSVMV. This is Scsvmv university. This is Tamilnadu"

print(word_tokenize(example_text))
print(sent_tokenize(example_text))

for i in word_tokenize(example_text):
   fi print(i)
