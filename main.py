def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)
    character_count = count_characters(text)
    
    print_report(book_path, word_count, character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    character_dict = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return character_dict


def print_report(book_path, word_count, character_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Sort character count dictionary by count in descending order
    sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


main()