def is_prime(n):
    if n <= 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
        return True

try:
    n = int(input("Enter number: "))
    print(is_prime(n))

except ValueError as c:
    print(c)