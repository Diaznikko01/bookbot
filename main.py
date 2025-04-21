import sys
from stats import get_word_count 
from stats import sort_char_count


if len(sys.argv) < 2:
    print("Usage: python3 main.py <filepath>")
    sys.exit(1)


filepath = sys.argv[1]
book_contents = ""


with open(filepath, "r") as f:
    book_contents = f.read()


sorted_char_count = sort_char_count(book_contents)


def main():
    print("===============BOOKBOT===============")
    print("")
    print("==========GENERATING REPORT==========")
    print(f"{get_word_count(book_contents)} WORDS IN BOOK")
    print("-------------------------------------")
    for dict in sorted_char_count:
        char = dict["char"]
        num = dict["count"]
        print(f"{char}: {num}")
    print("=====================================")


main()