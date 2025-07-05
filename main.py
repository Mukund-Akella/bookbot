import sys

from stats import num_words
from stats import character_dictionary
from stats import sort_dicts
from stats import transform_dict_to_list
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    word_count = num_words(text)
    char_dict = character_dictionary(text)
    sorted_dict = transform_dict_to_list(char_dict)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_dict:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
        else:
            continue
    print("============= END ===============")




main() 

