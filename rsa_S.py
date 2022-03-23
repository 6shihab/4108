import math
import sympy as sym

p = int(input("Insert a Prime number p: "))
while not sym.isprime(p):
    p = int(input("You enter a non prime number again Insert a Prime number p: "))

q = int(input("Insert another Prime Number q: "))
while not sym.isprime(q):
    q = int(input("You enter a non prime number again Insert a Prime number q: "))

n = p*q
phi = (p-1)*(q-1)

print("Values of e: ")
for e in range(2, n):
    if math.gcd(e, phi) == 1:
        print(e, end=" ")

print("")
e = int(input("insert the value of e: "))

for d in range(2, phi):
    if (d * e) % phi == 1:
        break

msg = 192


C=(msg**e)%n
M=(C**d)%n


print(C)
print(M)

