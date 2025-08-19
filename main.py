import sys
from stats import (
    get_word_count,
    get_char_count,
    get_sorted_list_of_char_count,
)


def main():
    path_error()
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_count_unsorted_dict = get_char_count(text)  # unsorted dictionary
    char_count_sorted_list = get_sorted_list_of_char_count(text)
    print_result(path, word_count, char_count_sorted_list)
    # print(text)
    # print(f"{word_count} words found in the document")
    # print(char_count_unsorted_dict)


def path_error():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_result(path, word_count, char_count_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count_sorted_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
