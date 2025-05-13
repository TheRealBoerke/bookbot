def sort_on(dict):
    return dict["num"]    

def count_words_in_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    return num_words

def count_chars_in_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
    num_chars = {}
    for char in file_contents:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_char_count(num_char_dict):
    sorted_charcount = []
    for key in num_char_dict.keys():
        sorted_charcount.append({"char": key, "num": num_char_dict[key]})
    sorted_charcount.sort(reverse=True, key=sort_on)
    return sorted_charcount