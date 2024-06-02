def is_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return False

    possible_triangle_length = [a, b, c]
    longest_side = max(possible_triangle_length)
    del possible_triangle_length[possible_triangle_length.index(longest_side)]

    sum_of_two_shorter_sides = sum(possible_triangle_length)

    return longest_side < sum_of_two_shorter_sides
