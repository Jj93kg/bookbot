import sys
from stats import num_words, num_unique_chars, sort_on, sort_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = num_words(book_text)
    char_counts = num_unique_chars(book_text)
    sorted_chars = sort_chars(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")  
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")

main()