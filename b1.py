num = [(4105, 10), (4539, 6)]

for a, b in num:
    print(a,b)
    gcd = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    print(f"GCD for {a} and {b} is {gcd}")