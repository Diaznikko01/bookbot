from stats import get_word_count
from stats import sort_list
import sys

if len(sys.argv) < 2:
    print("'Usage: python3 main.py <path_to_book>'")
    sys.exit(1)

filepath = sys.argv[1]

def main():
    word_count = get_word_count(filepath)
    sorted_list = sort_list(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")   
    print(f"Found {word_count} total words") 
    print("--------- Character Count -------")
    for char in sorted_list:
        character = char["char"]
        count = char["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")
        
main()
