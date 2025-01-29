from random_word import RandomWords
import nltk
from nltk.corpus import wordnet as wn
from time import sleep

# Download necessary nltk data
nltk.download('wordnet')
nltk.download('omw-1.4')

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
            # Generate a meaningful example sentence
            example_sentence = f"The use of '{word}' in daily conversation enhances vocabulary."

        # Fetch synonyms & antonyms
        synonyms = set()
        antonyms = set()
        for syn in synsets:
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace("_", " "))
                if lemma.antonyms():
                    antonyms.add(lemma.antonyms()[0].name().replace("_", " "))

        # Print synonyms & antonyms
        synonyms = ", ".join(list(synonyms)[:5]) if synonyms else "None"
        antonyms = ", ".join(list(antonyms)[:5]) if antonyms else "None"

        print(f"📖 Synonyms: {synonyms}")
        print(f"📖 Antonyms: {antonyms}")
    else:
        print("📖 Meaning: Not found.")
        example_sentence = f"The word '{word}' is interesting to learn."
        synonyms = "None"
        antonyms = "None"

    # Print improved example sentence
    print(f"✍️ Example: {example_sentence}")

    # Sleep to avoid excessive API calls
    sleep(1)
