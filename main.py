import sys
from stats import count_words, count_character, sort_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def generate_book_report(filepath):
    book_text = get_book_text(filepath)
    char_count = sort_dictionary(count_character(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        generate_book_report(sys.argv[1])


main()
