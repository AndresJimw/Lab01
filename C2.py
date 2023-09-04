import math

def is_prime(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True

def result(M, e, p):
    result = math.pow(M,e) % p
    return result

M = 8
e = 5
p = 269

if is_prime(p):
    r = result(M, e, p)
    print(f"The number 'p'= {p} is prime.")
    print(f"The result of M^e mod p is {r}")
else:
    print(f"The number 'p'={p} is not prime.")
