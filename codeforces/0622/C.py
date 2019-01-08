from sys import stdin, stdout

n, m = map(int, input().split())

a = [0]

a.extend(list(map(int, stdin.readline().split())))

a[0] = a[1] + 1

p = list(range(n + 1))

i, j = n, n
while i > 0:
	while a[i] == a[j] and j >= 0:
		j -= 1
	for k in range(j + 1, i + 1):
		p[k] = j
	i = j

for _ in range(m):
	l, r, x = map(int, stdin.readline().split())
	if a[r] != x:
		stdout.write(str(r))
	else:
		if p[r] >= l:
			stdout.write(str(p[r]))
		else:
			stdout.write('-1')
	stdout.write('\n')
