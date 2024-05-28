def high_and_low(numbers: str):
    numbers_int_list = [int(x) for x in numbers.split(" ")]
    return str(max(numbers_int_list)) + " " + str(min(numbers_int_list))
