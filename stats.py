

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        print(f"Error encountered {e}")
        return ""

def get_word_count(filepath):
    
    book = get_book_text(filepath)
    words = book.split()
    word_count = len(words)
    return word_count

def get_char_count(filepath):
    character_count = {}
    book = get_book_text(filepath)
    all_lower = book.lower()
    for character in all_lower:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count
    
def sort_on(dict):
    return dict["count"]

def sort_list(filepath):
    char_dict = get_char_count(filepath)
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


    
        
