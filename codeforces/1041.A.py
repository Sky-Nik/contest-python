n = int(input())

a = list(map(int, input().split()))

print(max(a) - min(a) - len(a) + 1)
