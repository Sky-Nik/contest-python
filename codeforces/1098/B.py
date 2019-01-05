n, m = map(int, input().split())

table = [input() for _ in range(n)]

print(table)

pairs = [('AC', 'GT'), ('AG', 'CT'), ('AT', 'CG'), ('CG', 'AT'), ('CT', 'AG'), ('GT', 'AC')]

d = {}

# h
for pair in pairs:
	diff = 0
	for i in range(n):
		_pair = pair[i % 2]

		diff_1 = 0
		for j in range(m):
			if table[i][j] != _pair[j % 2]:
				diff_1 += 1

		diff_2 = 0
		for j in range(m):
			if table[i][j] != _pair[1 ^ (j % 2)]:
				diff_2 += 1

		diff += min(diff_1, diff_2)

	d[('h', pair)] = diff

# v
for pair in pairs:
	diff = 0
	for j in range(m):
		_pair = pair[j % 2]

		diff_1 = 0
		for i in range(n):
			if table[i][j] != _pair[i % 2]:
				diff_1 += 1

		diff_2 = 0
		for i in range(n):
			if table[i][j] != _pair[1 ^ (i % 2)]:
				diff_2 += 1

		diff += min(diff_1, diff_2)

	d[('v', pair)] = diff

h_v, PAIR = None, None
for k, v in d.items():
	if v ==  min(d.values()):
		h_v, PAIR = k
		break

if h_v == 'h':
	for i in range(n):
		pair = PAIR[i % 2]

		diff_1 = 0
		for j in range(m):
			if table[i][j] != pair[j % 2]:
				diff_1 += 1

		diff_2 = 0
		for j in range(m):
			if table[i][j] != pair[1 ^ (j % 2)]:
				diff_2 += 1

		if diff_1 < diff_2:
			for j in range(m):
				table[i][j] = pair[j % 2]
		else:
			for j in range(m):
				table[i][j] = pair[1 ^ (j % 2)]

if h_v == 'v':
	for j in range(m):
		pair = PAIR[j % 2]

		diff_1 = 0
		for i in range(n):
			if table[i][j] != pair[i % 2]:
				diff_1 += 1

		diff_2 = 0
		for i in range(n):
			if table[i][j] != pair[1 ^ (i % 2)]:
				diff_2 += 1

		if diff_1 < diff_2:
			for i in range(n):
				table[i][j] = pair[i % 2]
		else:
			for i in range(n):
				table[i][j] = pair[1 ^ (i % 2)]

print(answer)
