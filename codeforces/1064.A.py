abc = tuple(map(int, input().split()))

print(2 * max(abc) - sum(abc) + 1 if 2 * max(abc) >= sum(abc) else 0)
