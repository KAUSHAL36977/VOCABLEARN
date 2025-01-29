from random_word import RandomWords
from PyDictionary import PyDictionary
import nltk
from time import sleep

nltk.download('punkt')

# Initialize objects
r = RandomWords()
dictionary = PyDictionary()

# Generate 10 unique random words
unique_words = set()
while len(unique_words) < 10:
    word = r.get_random_word()
    if word:
        unique_words.add(word)

# Process each word
for word in unique_words:
    print(f"\n🔹 Word: {word.capitalize()}")
    
    # Get meaning
    meaning = dictionary.meaning(word)
    if meaning:
        first_meaning = list(meaning.values())[0][0]  # Get first available meaning
        print(f"📖 Meaning: {first_meaning}")
    else:
        print("📖 Meaning: Not found.")
    
    # Generate a sentence (fallback if no example is found)
    example_sentence = f"The word '{word}' is interesting to learn."
    
    # Print example sentence
    print(f"✍️ Example: {example_sentence}")

    # Sleep to avoid rate limiting (if using API-based dictionary)
    sleep(1)
