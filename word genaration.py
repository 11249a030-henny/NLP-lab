import nltk

def generate_words(word):
    # Plural form
    if word.endswith('y'):
        plural = word[:-1] + "ies"
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        plural = word + "es"
    else:
        plural = word + "s"

    # Present participle
    if word.endswith('e') and not word.endswith('ee'):
        ing = word[:-1] + "ing"
    else:
        ing = word + "ing"

    # Past tense
    if word.endswith('e'):
        past = word + "d"
    else:
        past = word + "ed"

    print("\nGenerated Word Forms")
    print("----------------------")
    print("Root Word :", word)
    print("Plural Form :", plural)
    print("Present Participle :", ing)
    print("Past Tense :", past)

word = input("Enter a root word: ").lower()
generate_words(word)
