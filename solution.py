def sum_str(a: str, b: str):
    if a == "" and b == "":
        return "0"

    if a == "" and len(b) > 0:
        return b

    if len(a) > 0 and b == "":
        return a

    return "".join(str(int(a) + int(b)))
