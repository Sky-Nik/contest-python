# https://www.hackerrank.com/challenges/security-encryption-scheme/problem
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)


print(factorial(int(input())))
