def get_word_count(book_contents):
    words = book_contents.split()
    word_count = len(words)
    return word_count


def get_char_count(book_contents):
    char_count = {}
    lower_book_contents = book_contents.lower()
    for char in lower_book_contents:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_on(dict):
    return dict["char"]


def sort_char_count(book_contents):
    char_count = get_char_count(book_contents)
    sorted_char_count = []
    for key, value in char_count.items():
        if key.isalpha():
            sorted_char_count.append({"char": key, "count": value})
    sorted_char_count.sort(key=sort_on)
    return sorted_char_count



