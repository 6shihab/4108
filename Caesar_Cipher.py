def encrypt(string, shift):
    cipher = ' '
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher


def decrypt(cipher, shift):
    plain = ''
    for char in cipher:
        if char == ' ':
            plain = plain + char
        elif char.isupper():
            plain = plain + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            plain = plain + chr((ord(char) - shift - 97) % 26 + 97)

    return plain


text = "Hello Shihab"
s = 2
print("Original string: ", text)
plain = encrypt(text, s)
print("After encryption: ", encrypt(text, s))
print("After decryption :", decrypt(plain, s))
