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

for e in range(2,Qn):
    if gcd(e,Qn) == 1:
        break
print('n = '+str(n) + '\n')
print('Qn = '+str(Qn) + '\n')
print('e = '+str(e) + '\n')

for i in range(e, 100):
    x = 1 + i * Qn
    if x % e == 0:
        d = int(x / e)
        break
print('d = '+str(d))
print('Public Key = '+'('+str(e)+','+ str(n)+')')
print('Private Key = '+'('+str(d)+','+ str(n)+')')
M = int(input('Enter the value of text = '))

C=(pow(M,e) % n)
print('Cipher Text is = '+str(C))

PT=(pow(C,d) % n)
print('Decrypted Plaintext ='+str(PT))


