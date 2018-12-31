n, a = int(input()), list(map(int, input().split()))

print(min(sum(2 * a[i] * (abs(x - i) + i + x) for i in range(n)) for x in range(n)))
