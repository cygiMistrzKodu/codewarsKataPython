import re


def disemvowel(string_):
    return re.sub("[aAeEiIoOuU]", "", string_)
