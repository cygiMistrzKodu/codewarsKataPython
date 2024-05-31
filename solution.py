import math


def century(year):
    century_in = year / 100

    if century_in.is_integer():
        return century_in
    else:
        return math.floor(century_in) + 1
