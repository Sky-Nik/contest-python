n = int(input())

print(n + (10 - n % 10) if n % 10 > 5 else 10 * (n // 10))
