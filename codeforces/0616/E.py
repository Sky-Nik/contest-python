from math import floor, sqrt

mod = 10**9 + 7


def _sum(n):
	return (n * (n + 1) // 2) % mod


def __sum(lf, rg):
	return (_sum(rg) - _sum(lf - 1)) % mod


def calcDiv(n, m):
	m = min(n, m)

	ans, minVal = 0, m
	
	for i in range(1, floor(sqrt(n)) + 1):
		lf, rg = n // (i + 1), n // i

		rg = min(rg, m)

		if lf >= rg:
			continue

		minVal = lf

		ans += i * __sum(lf + 1, rg)
		ans %= mod

	for i in range(1, minVal + 1):
		ans += n // i * i
		ans %= mod

	return ans


n, m = map(int, input().split())

print((n * m - calcDiv(n, m)) % mod)
