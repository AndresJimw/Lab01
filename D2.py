
def is_prime(val):
    if val <= 1:
        return False
    if val <= 3:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False
    i = 5
    while i * i <= val:
        if val % i == 0 or val % (i + 2) == 0:
            return False
        i += 6
    return True

prime_numbers = []
for val in range(1, 1001):
    if is_prime(val):
        prime_numbers.append(val)

print("Prime numbers:")
print(prime_numbers)
print("Highest prime number:")
print(max(prime_numbers))
