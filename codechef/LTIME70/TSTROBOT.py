t = int(input())

for ti in range(t):
	n, x = map(int, input().split())
	s = input().strip()
	
	low, high = x, x
	
	for c in s:
		if c == 'L':
			x -= 1
			low = min(low, x)
		if c == 'R':
			x += 1
			high = max(high, x)
	
	print(high - low + 1)
