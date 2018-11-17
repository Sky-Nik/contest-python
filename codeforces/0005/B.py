from sys import stdin

lines = list(map(lambda _: _.strip(), stdin.readlines()))

max_len = max(list(map(len, lines)))

print((max_len + 2) * '*')

left = 0

for line in lines:
	pad = max_len - len(line)

	if pad % 2 != 0:
		left_pad = pad // 2 + left
		left = 1 - left
	else:
		left_pad = pad // 2

	right_pad = pad - left_pad

	print('*', left_pad * ' ', line, right_pad * ' ', '*', sep='')

print((max_len + 2) * '*')
