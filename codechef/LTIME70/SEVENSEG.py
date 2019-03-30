digits = [
	0b1110111,  # 0
	0b0010010,  # 1
	0b1011101,  # 2
	0b1011011,  # 3
	0b0111010,  # 4
	0b1101011,  # 5
	0b1101111,  # 6
	0b1010010,  # 7
	0b1111111,  # 8
	0b1111011,  # 9
]

t = int(input())

for ti in range(t):
	n = int(input())
	
	x, y = [None for _ in range(n)], [None for _ in range(n)]

	for i in range(n):
		x[i], y[i] = map(int, input().split())

	any_ok = False
	min_dead, max_dead = 7, 0

	for mask in range(1 << 7):
		ok = True

		for i in range(n):
			if bin(digits[x[i]] & mask).count('1') != y[i]:
				ok = False

		if ok:
			any_ok = True
			num_dead = 7 - bin(mask).count('1')
			min_dead = min(min_dead, num_dead)
			max_dead = max(max_dead, num_dead)

	if any_ok:
		print(min_dead, max_dead)
	else:
		print('invalid')
