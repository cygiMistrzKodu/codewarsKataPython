def sum_square_digits(digits):
    square_sum = 0
    for digit in digits:
        square_sum += digit * digit
    return square_sum


def repeat_sequence_len(n):
    number_string = str(n)

    square_sum_list = []
    digits = list(map(int, number_string.strip()))
    square_sum_repeat_start_sequence_number = -10

    while square_sum_repeat_start_sequence_number < 0:
        for i in range(0, 100):
            digit_square_sum = sum_square_digits(digits)
            square_sum_list.append(digit_square_sum)
            digits_string = str(digit_square_sum)
            digits = list(map(int, digits_string.strip()))

        for number in square_sum_list:
            number_of_occurance = square_sum_list.count(number)
            if number_of_occurance >= 2:
                square_sum_repeat_start_sequence_number = number
                break

    repeat_sequence_first_occurrence_index = square_sum_list.index(square_sum_repeat_start_sequence_number)
    repeat_sequence_second_occurrence_index = square_sum_list.index(square_sum_repeat_start_sequence_number,
                                                                    repeat_sequence_first_occurrence_index + 1)

    repeat_sequence_length = len(square_sum_list[
                                 repeat_sequence_first_occurrence_index:repeat_sequence_second_occurrence_index])
    return repeat_sequence_length

