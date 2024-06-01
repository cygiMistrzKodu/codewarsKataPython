import re


def printer_error(s):
    error_string_count = len(re.findall("[n-z]", s))
    return str(error_string_count) + "/" + str(len(s))
