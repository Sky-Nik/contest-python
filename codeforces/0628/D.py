mod, N = int(1e9 + 7), 2010

m, d = map(int, input().split())

a = list(map(int, list(input())))

b = list(map(int, list(input())))


z = [[[0, 0] for j in range(N)] for i in range(N)]

def f(s):
	n = len(s)

	for i in range(n + 1):
		for j in range(m):
			for k in (0, 1):
				z[i][j][k] = 0
	
	z[0][0][1] = 1

	for i in range(n):
		for j in range(m):
			for k in (0, 1):
				for p in range((s[i] if k else 9) + 1):
					if (i % 2 == 1) and p != d:
						continue

					if (i % 2 == 0) and p == d:
						continue

					if i == 0 and p == 0:
						continue

					ni = i + 1
					nj = (j * 10 + p) % m
					nk = int(bool(k) and (p == s[i]))

					z[ni][nj][nk] += z[i][j][k]
					z[ni][nj][nk] %= mod

	return sum(z[n][0]) % mod


def g(s):
	rm = 0

	for i in range(len(s)):
		if (i % 2 == 1) and s[i] != d:
			return 0
		if (i % 2 == 0) and s[i] == d:
			return 0
		rm = (rm * 10 + s[i]) % m

	return int(not bool(rm))


print((f(b) - f(a) + g(a)) % mod)
