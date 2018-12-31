n, k = map(int, input().split())

print('YES' if (n // k + 1) // 2 > (n // (2 * k)) else 'NO')
