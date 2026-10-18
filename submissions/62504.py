def starts_with_vowel(text):
    """Return True if the given text starts with a vowel (a, e, i, o, u).

    The check is case-insensitive. An empty string returns False.
    """
    if not text:
        return False
    return text[0].lower() in "aeiou"


if __name__ == "__main__":
    print(starts_with_vowel("apple"))   # True
    print(starts_with_vowel("banana"))  # False
    print(starts_with_vowel("Orange"))  # True
    print(starts_with_vowel(""))        # False
