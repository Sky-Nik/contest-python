line = input().strip()

d, c = [-1 for char in line], [-1 for char in line]

stack = []

for i, char in enumerate(line):
	if char == '(':
		stack.append(i)
	else:  # if char == ')':
		if not stack:
			c[i] = -1
			d[i] = -1
		else:  # if stack:
			d[i] = stack.pop()
			if line[d[i] - 1] == ')' and c[d[i] - 1] != -1:
				c[i] = c[d[i] - 1]
			else:
				c[i] = d[i]

# print(f'c={c};d={d}')

max_length = max(_ - c[_] if c[_] != -1 else -1 for _ in range(len(line)))

count_max = sum(1 if _ - c[_] == max_length and c[_] != -1 else 0 for _ in range(len(line)))

if max_length == -1:
	print('0 1')
else:
	print(max_length + 1, count_max)
