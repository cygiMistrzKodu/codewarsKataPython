from functools import reduce


def find_difference(a: list[int], b: list[int]):
    volume_a = reduce((lambda x, y: x * y), a)
    volume_b = reduce((lambda x, y: x * y), b)

    difference = volume_a - volume_b

    if difference < 0:
        return difference * -1
    else:
        return difference
