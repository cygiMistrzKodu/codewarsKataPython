def fake_bin(x: str):
    binary_string = []
    for digit in x:
        integer_digit = int(digit)

        if integer_digit < 5:
            binary_string.append("0")
        else:
            binary_string.append("1")

    return "".join(binary_string)
