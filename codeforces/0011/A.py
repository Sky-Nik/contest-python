from math import ceil

n, d = map(int, input().split())

b = list(map(int, input().split()))

a = 0

for i in range(1, n):
	if b[i] <= b[i - 1]:
		ai = ceil((b[i - 1] + 1 - b[i]) / d)
		a += ai
		b[i] += ai * d 

print(a)
