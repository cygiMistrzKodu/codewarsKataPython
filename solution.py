import re


def solution(s):
    words = re.findall("[a-z]*[a-z]|[A-Z][a-z]*", s)
    return " ".join(words)
