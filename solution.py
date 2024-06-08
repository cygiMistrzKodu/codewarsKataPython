def number(lines):
    return [str(word_number) + ": " + word for word_number, word in enumerate(lines, 1)]
