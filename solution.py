big_letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
               "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
               "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}


def shift_letter(sign: str, shift: int):
    if sign.isupper() and sign.isalpha():

        original_letter_position = big_letters[sign]
        new_letter_position = original_letter_position + shift
        if new_letter_position > 26:
            new_letter_position = new_letter_position - 26

        moved_letter = list(big_letters.keys())[list(big_letters.values()).index(new_letter_position)]

        return moved_letter
    else:
        return sign


def replace_digit_by_complement_to_9(sign: str):
    if sign.isdigit():
        digit_complement = 9 - int(sign)
        return str(digit_complement)
    else:
        return sign


def play_pass(s, n):
    shifted_string = "".join(shift_letter(letter, n) for letter in s)
    digit_replaced_string = "".join(replace_digit_by_complement_to_9(letter) for letter in shifted_string)

    string_with_lower_and_upper_letter = ""
    for sign_index in range(len(digit_replaced_string)):
        if digit_replaced_string[sign_index].isupper():
            if sign_index % 2 != 0:
                lower_letter = digit_replaced_string[sign_index].lower()
                string_with_lower_and_upper_letter += lower_letter
            else:
                string_with_lower_and_upper_letter += digit_replaced_string[sign_index]
        else:
            string_with_lower_and_upper_letter += digit_replaced_string[sign_index]

    return string_with_lower_and_upper_letter[::-1]
