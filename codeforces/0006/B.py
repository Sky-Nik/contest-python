n, m, c = input().split()

n, m = int(n), int(m)

b = [input().strip() for _ in range(n)]

a = set()

for i in range(n):
	for j in range(m):
		if (
			i > 0 and b[i - 1][j] == c or 
			i + 1 < n and b[i + 1][j] == c or
			j > 0 and b[i][j - 1] == c or
			j + 1 < m and b[i][j + 1] == c
		):
			a.add(b[i][j])

a -= {'.', c}

print(len(a))
