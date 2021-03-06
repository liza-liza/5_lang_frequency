import sys
import re
import collections


def load_data(file_path):
    try:
        with open(file_path, 'r') as loaded_file:
            return loaded_file.read()

    except FileNotFoundError:
        return None


def get_most_frequent_words(parsed_file, how_many_words=10):
    words_list = re.findall(r'\w+', parsed_file.lower())
    return collections.Counter(words_list).most_common(how_many_words)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        loaded_file = load_data(sys.argv[1])

        if not loaded_file:
            print("File or direcory {} not found".format(sys.argv[1]))
        else:
            most_common_words = get_most_frequent_words(loaded_file)
            print("Most сommon words in the {} are (word, frequency):"
                  .format(sys.argv[1]))
            for word, frequency in most_common_words:
                print('{:.<20}{:<3}'.format(word, frequency))

    else:
        print("Using: python3 lang_frequency.py <path_to_file>")
