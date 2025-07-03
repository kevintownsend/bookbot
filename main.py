from stats import get_num_words
from stats import get_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    full_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(full_text)
    print(f"{num_words} words found in the document")
    num_chars = get_num_chars(full_text)
    print(num_chars)

main()
