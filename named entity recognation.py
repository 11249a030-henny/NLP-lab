import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("The 'en_core_web_sm' model is not installed.")
    print("Install it using:")
    print("python -m spacy download en_core_web_sm")
    exit()

# Get input from the user
text = input("Enter a sentence: ")

# Process the text
doc = nlp(text)


print("\nNamed Entities")
print("-" * 40)

if doc.ents:
    for ent in doc.ents:
        print(f"Entity : {ent.text}")
        print(f"Label  : {ent.label_}")
        print("-" * 40)
else:
    print("No named entities found.")
