def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letters = get_chars_dict(text)
    letter_list = dict_to_list(letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in letter_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["char"]


def dict_to_list(letters):
    word_list = []
    for ch in letters:
        word_list.append({"char": ch, "num": letters[ch]})
    word_list.sort(key=sort_on)
    return word_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()