from decimal import Decimal

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

p = int(input('Enter the value of p = '))
q = int(input('Enter the value of q = '))

n = p * q
Qn = (p - 1) * (q - 1)

for e in range(2, Qn):
    if gcd(e, Qn) == 1:
        break
print('n = ', n)
print('Qn = ', Qn)
print('e = ', e)

d = 1
while 1:
    if (d * e) % Qn == 1:
        break
    d += 1

print('d = ', d)
print('Public Key = ' + '(' + str(e) + ',' + str(n) + ')')
print('Private Key = ' + '(' + str(d) + ',' + str(n) + ')')
M = int(input('Enter the value of text = '))

C = (pow(M, e) % n)
print('Cipher Text is = ', C)

PT = (pow(C, d) % n)
print('Decrypted Plaintext =', PT)
