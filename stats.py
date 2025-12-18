def num_words(book_text):
    words = book_text.split()
    return len(words)

def num_unique_chars(book_text):
    char_counts = {}
    for char in book_text:
        char = char.lower()
        if (char not in char_counts):
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return (char_counts)

def sort_on(item):
    return (item["num"])

def sort_chars(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(key=sort_on, reverse=True)
    return (char_list)