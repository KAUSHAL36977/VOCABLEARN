import nltk
from nltk.corpus import words

nltk.download('words')

# Get the list of English words
word_list = words.words()
print(len(word_list))  # Number of words
print(word_list[:10])  # Sample words
