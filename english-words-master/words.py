# Install required libraries
!pip install nltk PyDictionary wonderwords

# Import necessary libraries
import nltk
import random
from nltk.corpus import words
from PyDictionary import PyDictionary
from wonderwords import RandomSentence

# Step 1: Download the words corpus for nltk if not already downloaded
def download_nltk_corpus():
    nltk.download('words')

# Step 2: Initialize the PyDictionary
def initialize_dictionary():
    return PyDictionary()

# Step 3: Get the list of words from the nltk corpus
def get_nltk_words():
    return words.words()

# Step 4: Fetch 10 random words with valid meanings from the nltk corpus
def get_random_words_with_meanings(word_list, dictionary, num_words=10):
    sample_words = []
    while len(sample_words) < num_words:
        random_word = random.choice(word_list)
        meaning = dictionary.meaning(random_word)
        if meaning:  # Check if PyDictionary has an entry for the word
            sample_words.append((random_word, meaning))
    return sample_words

# Step 5: Generate example sentences for each word using wonderwords
def generate_example_sentence(word):
    sentence_generator = RandomSentence()
    return sentence_generator.sentence()

# Step 6: Display words, meanings, and example sentences
def display_words_with_details(word_list):
    for word, meaning in word_list:
        print(f"Word: {word}")
        print(f"Meaning: {meaning}")
        example_sentence = generate_example_sentence(word)
        print(f"Example Sentence: {example_sentence}")
        print("-" * 50)

# Main function to execute the program
def main():
    # Step 1: Download the nltk corpus
    download_nltk_corpus()

    # Step 2: Initialize the dictionary
    dictionary = initialize_dictionary()

    # Step 3: Get the list of words from nltk
    nltk_word_list = get_nltk_words()

    # Step 4: Fetch 10 random words with meanings
    random_words_with_meanings = get_random_words_with_meanings(nltk_word_list, dictionary)

    # Step 5: Display the results
    print("Daily 10 New Words with Meanings and Example Sentences:")
    display_words_with_details(random_words_with_meanings)

# Run the program
if __name__ == "__main__":
    main()
