def count_words(str):
    words = len(str.split())
    return words


def count_character(str):
    char_count = {}
    for char in str.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def sort_dictionary(dict):
    sorted_dictionary = []
    for char in dict:
        sorted_dictionary.append({"char": char, "num": dict[char]})
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary
