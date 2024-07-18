def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(text)
    
    word_count = count_words(text)
    print(f"\nThe book contains {word_count} words.")
    
    character_count = count_characters(text)
    print("\nCharacter count:")
    print(character_count)


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


main()