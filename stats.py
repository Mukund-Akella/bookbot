def num_words(book):
    words = book.split()
    return len(words)

def character_dictionary(book):
    characters = book.lower()
    characters_list = characters.lower()
    dict = {}
    for character in characters:
        if character in dict:
            dict[character]+=1
        else:
            dict[character] = 1
    return dict

def sort_dicts(dict):
    return dict.sort(reverse=True)


def sort_list(dict):
    return dict["num"]

def transform_dict_to_list(char_dict):
    result = []
    for char, count in char_dict.items():
        result.append({"char": char, "num": count})
    result.sort(reverse=True, key=sort_list)
    return result
