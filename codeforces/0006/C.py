n = int(input())

t = list(map(int, input().split()))

p, s = [0 for _ in range(n)], [0 for _ in range(n)]

for i in range(1, n):
	p[i] = p[i - 1] + t[i - 1]

for i in range(n - 2, -1, -1):
	s[i] = s[i + 1] + t[i + 1]

a, b = 0, 0

for i in range(n):
	if p[i] <= s[i]:
		a += 1
	else:
		b += 1

print(a, b)
