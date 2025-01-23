import nltk
from nltk.corpus import words

nltk.download('words')

# Get the list of English words
word_list = words.words()
print(len(word_list))  # Number of words
print(word_list[:10])  # Sample words
# Importing nltk and downloading the word corpus
import nltk
from nltk.corpus import words
nltk.download('words')

# Importing PyDictionary for word meanings, synonyms, and antonyms
from PyDictionary import PyDictionary
dictionary = PyDictionary()

# Importing pyenchant for spell checking and dictionary lookups
import enchant


import nltk
import random
from nltk.corpus import words
from PyDictionary import PyDictionary
import enchant

# Download the words corpus for nltk if not already downloaded
nltk.download('words')

# Initialize dictionary for PyDictionary and pyenchant
dictionary = PyDictionary()
enchant_dict = enchant.Dict("en_US")

# Get words from nltk
nltk_words = words.words()

# Function to get words from pyenchant
def get_enchant_words():
    sample_words = []
    while len(sample_words) < 10:
        random_word = random.choice(nltk_words)
        if enchant_dict.check(random_word):  # Ensure word is valid in pyenchant
            sample_words.append(random_word)
    return sample_words

# Function to get words from PyDictionary (fallback on nltk word list)
def get_pydictionary_words():
    sample_words = []
    while len(sample_words) < 10:
        random_word = random.choice(nltk_words)
        meaning = dictionary.meaning(random_word)
        if meaning:  # Check if PyDictionary has an entry for the word
            sample_words.append(random_word)
    return sample_words

# Get 10 random words from each source
nltk_sample = random.sample(nltk_words, 10)
enchant_sample = get_enchant_words()
pydictionary_sample = get_pydictionary_words()

# Print the results
print("Random 10 words from NLTK:", nltk_sample)
print("Random 10 words from PyDictionary:", pydictionary_sample)
print("Random 10 words from pyenchant:", enchant_sample)


