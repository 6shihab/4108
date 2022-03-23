msg = "hello bangladesh"
key = "shihab"
cipher = ''
for i in range(len(msg)):
    cipher += chr((ord(msg[i]) + ord(key[i % len(key)])) % 26+65)
print(cipher)
