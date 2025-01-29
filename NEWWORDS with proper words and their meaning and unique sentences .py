!pip install random-word nltk


!pip install -U textblob
import nltk
nltk.download('punkt_tab')


from random_word import RandomWords
import nltk
from nltk.corpus import wordnet as wn
from textblob import TextBlob
from time import sleep

# Download necessary nltk data
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab') # Download punkt_tab resource

# Initialize the random word generator
r = RandomWords()

# Generate 10 unique, valid words
unique_words = set()
while len(unique_words) < 10:
    word = r.get_random_word()
    
    # Validate if the word exists in WordNet (to avoid gibberish)
    if word and wn.synsets(word):
        unique_words.add(word)

# Process each word
for word in unique_words:
    print(f"\n🔹 Word: {word.capitalize()}")

    # Get meaning
    synsets = wn.synsets(word)
    if synsets:
        first_meaning = synsets[0].definition()
        print(f"📖 Meaning: {first_meaning}")

        # Get example sentence from WordNet if available
        if synsets[0].examples():
            example_sentence = synsets[0].examples()[0]
        else:
            # Generate a sentence using TextBlob
            example_sentence = TextBlob(word).sentences[0].string.capitalize() + "."
    else:
        print("📖 Meaning: Not found.")
        example_sentence = f"The word '{word}' is interesting to learn."

    # Print example sentence
    print(f"✍️ Example: {example_sentence}")

    # Sleep to avoid excessive API calls
    sleep(1)
