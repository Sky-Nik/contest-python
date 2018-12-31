a1, a2, a3, a4 = map(int, input().split())

d = {'1': a1, '2': a2, '3': a3, '4': a4}

s = input()

print(sum(d[c] for c in s))
