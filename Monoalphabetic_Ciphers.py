import random

plain_text = []
key = []
for i in range(65, 65 + 26):
    plain_text.append(chr(i))
    key.append(chr(i))
random.shuffle(key)

message = "Hello Shihab"
print("Plain Text: ", plain_text)
print("Key:        ", key)

cipher = ''


for ch in message:
    if ch!=' ':
        index = plain_text.index(ch.upper())
        cipher = cipher + key[index]
    else:
        cipher = cipher + ch

print("Cipher: ", cipher)

decrypted_mess = ''
for ch in cipher:
    if ch!=' ':
        index = key.index(ch.upper())
        decrypted_mess = decrypted_mess + plain_text[index]
    else:
        decrypted_mess = decrypted_mess + ch

print("Decrypted Message: ", decrypted_mess)
