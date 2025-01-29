!pip install random-word

from random_word import RandomWords

r = RandomWords()
for i in range(10):
    print(r.get_random_word())  # Correct indentation
