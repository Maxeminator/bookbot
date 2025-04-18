import sys
from stats import get_book_words
from stats import get_book_symbols
from stats import sort_dictionary

def get_book_text(input):
    with open(input) as f:
        return f.read()
# or use text=f.read() <- it prints right after return without print in main

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text=get_book_text(sys.argv[1])
    words_num=get_book_words(text)
    chars=get_book_symbols(text)
    sorted_chars=sort_dictionary(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words_num} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()
