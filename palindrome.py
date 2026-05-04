from collections import deque


def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    chars = deque(cleaned)
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return "не палиндром"
    return "палиндром"


if __name__ == "__main__":
    strings = [
        "Тенет",
        "Дід і дід",
        "кит на морі романтик",
        "в переулок",
        "завтрак",
        "Діловите",
    ]

    for string in strings:
        print(f"строка: {string} - {is_palindrome(string)}")
