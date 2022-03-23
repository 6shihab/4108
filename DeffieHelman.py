from math import gcd
import sympy as sym

q = int(input("Enter a prime Number: "))
while not sym.isprime(q):
    q = int(input("You enter a non Prime number please enter a prime number: "))

print("Primitive root of ", q, " is: ")
for i in range(2, q, 1):
    if gcd(i, q - 1) == 1:
        print(i, end=" ")

alpha = int(input("\nChoose one of the primitive roots: "))

Xa = int(input("select User A Private Key: "))
public_key_of_user_a = pow(alpha, Xa) % q
print("Public Key of User A (q,alpha,Ya):(", q, alpha, public_key_of_user_a, ")")

Xb = int(input("select User B Private Key: "))
public_key_of_user_b = pow(alpha, Xb) % q
print("Public Key of User B (q,alpha,Yb):(", q, alpha, public_key_of_user_b, ")")

secret_key_of_user_a = pow(public_key_of_user_b, Xa) % q
secret_key_of_user_b = pow(public_key_of_user_a, Xb) % q

print("USER A Secret key = ", secret_key_of_user_a)
print("USER B Secret key = ", secret_key_of_user_b)
