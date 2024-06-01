def is_palindrome(s: str):
    lower_case_text = s.lower()

    return lower_case_text == lower_case_text[::-1]
