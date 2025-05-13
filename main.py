import sys
from stats import count_words_in_book
from stats import count_chars_in_book
from stats import sort_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    word_count = count_words_in_book(path_to_book)
    character_count = sort_char_count(count_chars_in_book(path_to_book))
    print("============ BOOKBOT ============")
    print(f"Analysis of book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in character_count:
        character = dict["char"]
        if character == "\n":
            character = "CR"
        count = dict["num"]
        print(f"{character}: {count}")
    print("============= END ===============")

main()