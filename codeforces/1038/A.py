n, k = map(int, input().split())
s = input().strip()
d = [0 for _ in range(k)]
for si in s:
    d[ord(si) - ord('A')] += 1
print(min(d) * k)
