
key_word = 'AYUSH'
message = "GEEKSFORGEEKS"

print("Message = ", message)

key_word_list = list(key_word)
key = ''
mess_len = len(message)
key_word_len = len(key_word)

for i in range(mess_len):
    key = key + key_word_list[(i % key_word_len)]

print("Key =     ", key)

key_list = list(key.upper())
mess_list = list(message.upper())

cipher_list = []
for i in range(mess_len):

    sum = (ord(key_list[i]) + ord(mess_list[i]) - (65 * 2)) % 26
    cipher_list.append(chr(sum + 65))

cipher = ''
for ch in cipher_list:
    cipher = cipher + ch

print("Cipher Text:", cipher)

dec_mess_list = []
for i in range(mess_len):
    sum = (ord(cipher_list[i].upper()) - ord(key_list[i].upper()) - (65 * 2)) % 26
    dec_mess_list.append(chr(sum + 65))

dec_mess = ''
for ch in dec_mess_list:
    dec_mess = dec_mess + ch

print("Decrypted Text:", dec_mess)
