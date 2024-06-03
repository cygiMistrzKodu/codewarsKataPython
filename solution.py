def get_middle(s):
    word_length = len(s)

    if word_length % 2 == 0:
        second_letter = int(word_length / 2)
        first_letter = second_letter - 1
        return s[first_letter] + s[second_letter]
    else:
        return s[int((word_length + 1) / 2) - 1]
