def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)

def get_char_count(w):
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

def get_num_words(w):
    t = w.split()
    return len(t)









if __name__ == '__main__':
    main()