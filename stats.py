def get_num_words(full_text):
    return len(full_text.split())

def get_num_chars(full_text):
    chars = {}
    for c in full_text:
        c = c.lower()
        if c in chars:
            chars[c] = chars[c] + 1
        else:
            chars[c] = 1
    return chars

