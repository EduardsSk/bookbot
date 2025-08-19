def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    characters = text.lower()
    char_dict = {}
    for char in characters:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


# Takes the dictionary of characters and their counts (get_char_count) and returns a sorted list of dictionaries
def get_sorted_list_of_char_count(text):
    unsorted_dict = get_char_count(text)
    list_dict = []
    for char, count in unsorted_dict.items():
        if char.isalpha():
            list_dict.append({"char": char, "num": count})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict


def sort_on(items):
    return items["num"]
