from sys import stdin

t, p = 0, 0

for line in stdin.readlines():
	line = line.strip()
	if line[0] == '+':
		p += 1
	elif line[0] == '-':
		p -= 1
	else:
		t += p * (len(line) - line.index(':') - 1)

print(t)
