# DAILY-10-NEW-WORDS-OF-ENGLISH-DICTIONARY-
DAILY 10 NEW AND INTERESTING WORDS OF ENGLISH FOR IMPROVING GRAMMER AND ENGLISH AS A LANGUAGE
# Random Word Generation Project

This project demonstrates the generation of random words using various Python libraries, including **NLTK**, **PyDictionary**, and **WonderWords**. The code provides methods to sample random words from different sources and validates them using tools like PyDictionary and pyenchant.

---

## Features

1. **Random Words from NLTK**
   - Fetches random words from the NLTK corpus.
   - Ensures that words are valid and unique.

2. **Random Words from PyDictionary**
   - Fetches random words and validates them using the PyDictionary library.
   - Ensures the word has a meaningful entry in the dictionary.

3. **Random Words from WonderWords**
   - Generates random words using the WonderWords library.
   - Simple and efficient.

4. **Random Words from PyEnchant (Optional)**
   - Validates random words against the PyEnchant dictionary (if installed).

---

## Requirements

Install the following libraries to run the project:

```bash
pip install nltk PyDictionary wonderwords pyenchant
```

---

## File Structure

```plaintext
random_word_generation
│
├── main.py         # Main Python script for generating random words
├── README.md       # Project documentation
└── requirements.txt # Dependencies for the project
```

---

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/random_word_generation.git
   cd random_word_generation
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python main.py
   ```

---

## Usage

### Generating Words from NLTK

The script uses the `nltk` library to fetch random words from its corpus. Ensure you download the required corpus before running:

```python
nltk.download('words')
```

### Generating Words from PyDictionary

The script uses `PyDictionary` to validate words and fetch their meanings:

```python
meaning = dictionary.meaning(random_word)
if meaning:
    print("Word is valid!")
```

### Generating Words from WonderWords

The `WonderWords` library generates random words without relying on a corpus:

```python
from wonderwords import RandomWord
r = RandomWord()
wonder_words = r.random_words(10)
```

---

## Example Output

```plaintext
Random 10 words from NLTK: ['word1', 'word2', ...]
Random 10 words from PyDictionary: ['word3', 'word4', ...]
Random 10 words from WonderWords: ['word5', 'word6', ...]
```

---

## Dependencies

- **nltk**: Natural Language Toolkit
- **PyDictionary**: Python wrapper for dictionary services
- **WonderWords**: Library for generating random words
- **pyenchant** (optional): Spellchecking library for Python

Install all dependencies using:

```bash
pip install nltk PyDictionary wonderwords pyenchant
```

---

## Notes

1. **NLTK Corpus**: Make sure to download the `words` corpus from NLTK before running the script.

2. **PyEnchant**: Some users may face installation issues with `pyenchant`. Ensure it is supported on your platform.

3. **Fallback Logic**: If PyDictionary fails to validate words, the script defaults to using NLTK words.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for feature suggestions and bug reports.

---

## Author

[Kaushal Kumar](mailto:kau333halkumar@gmail.com)

Happy Coding!
