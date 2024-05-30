import math


def find_next_square(sq: int):

    if math.isqrt(sq) ** 2 == sq:
        power = math.sqrt(sq)
        power += 1
        return power ** 2
    else:
        return -1
