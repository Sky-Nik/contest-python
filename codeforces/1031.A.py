w, h, k = map(int, input().split())

s, c = 0, 2 * (w + h - 2)

for _ in range(k):
	s += c
	c -= 16

print(s)
