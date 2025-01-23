#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <string>
#include <set>

// Function to read words from a file and store them in a vector
std::vector<std::string> load_words_from_file(const std::string& filename) {
    std::vector<std::string> word_list;
    std::ifstream file(filename);
    
    if (!file.is_open()) {
        std::cerr << "Could not open the file!" << std::endl;
        return word_list;
    }
    
    std::string word;
    while (file >> word) {
        word_list.push_back(word);
    }

    file.close();
    return word_list;
}

// Function to get a random word from the list
std::string get_random_word(const std::vector<std::string>& word_list) {
    int random_index = rand() % word_list.size();
    return word_list[random_index];
}

int main() {
    // Seed the random number generator
    srand(static_cast<unsigned int>(time(0)));

    // Load words from the dictionary file
    std::vector<std::string> word_list = load_words_from_file("dictionary.txt");

    if (word_list.empty()) {
        std::cerr << "No words loaded from the file!" << std::endl;
        return 1;
    }

    // Get the number of random words to print
    int num_words_to_print = 10; // You can change this to any number you want
    if (num_words_to_print > word_list.size()) {
        std::cerr << "Requested number of words exceeds available words. Adjusting to available count." << std::endl;
        num_words_to_print = word_list.size();
    }

    // Use a set to avoid printing duplicate words
    std::set<std::string> printed_words;

    std::cout << "Random " << num_words_to_print << " words:\n";
    for (int i = 0; i < num_words_to_print; ++i) {
        std::string random_word;
        do {
            random_word = get_random_word(word_list);
        } while (printed_words.find(random_word) != printed_words.end()); // Ensure no duplicates

        printed_words.insert(random_word);
        std::cout << random_word << std::endl;
    }

    return 0;
}
