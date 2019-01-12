prime = [True for _ in range(10**6)]

prime[0] = False

prime[1] = False

for i in range(2, 10**3):
	if prime[i]:
		for j in range(i, 10**6 // i):
			prime[i * j] = False

primes = list(filter(lambda _: prime[_] and _ > 11, range(10**6)))

p1 = [2, 3, 5]

t = int(input())

for ti in range(t):
	n = int(input())

	a = [1 for _ in range(n)]

	for i in range(n - 2):
		a[i] *= p1[i % 3]
		a[i + 1] *= p1[i % 3]

	a[-1] *= 7
	a[-2] *= 7

	a[-1] *= 11
	a[0] *= 11

	for i in range(n):
		a[i] *= primes[i]

	print(*a)
