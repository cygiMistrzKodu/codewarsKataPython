def xo(s: str):
    number_of_o = s.lower().count("o")
    number_of_s = s.lower().count("x")
    return number_of_o == number_of_s
