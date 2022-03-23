def caesar(plainText, shift):
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        elif ch== ' ':
            cipherText+=' '
    print ("Your ciphertext is: ", cipherText)
    return cipherText
caesar("Shihab HasanZ",2)