def gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n != 0:
        (m, n) = (n, m % n)
        print(m," ", n)
    return n


# calling function with parameters and printing it out
a = 368
b = 18

print(" GCD of given number is :", gcd(a, b))
