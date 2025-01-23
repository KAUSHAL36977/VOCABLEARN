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

