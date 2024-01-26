from string import ascii_letters


def encrypt(text, key):
    letters = ascii_letters
    result = ""

    for letter in text:
        if letter in letters:
            new_key = (letters.index(letter) + key) % 52
            result += letters[new_key]
        else:
            result += letter

    return result
