def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = 6
print(f"factorial of {n} is {factorial(n)}")