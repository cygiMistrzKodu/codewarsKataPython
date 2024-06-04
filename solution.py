def row_sum_odd_numbers(n):
    next_odd_number = 1
    count_odd_number_in_row = 0
    odd_sum = 0
    for triangle_row in range(0, n):
        count_odd_number_in_row += 1
        for index in range(0, count_odd_number_in_row):
            if count_odd_number_in_row > 1:
                next_odd_number += 2
            if triangle_row == n - 1:
                odd_sum += next_odd_number

    return odd_sum
