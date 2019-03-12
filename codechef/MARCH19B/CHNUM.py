T = int(input())

for t in range(T):
	N = int(input())

	A = list(map(int, input().split()))

	p, z, n = 0, 0, 0

	for a in A:
		if a > 0:
			p += 1
		elif a == 0:
			z += 1
		else:
			n += 1

	if z == 0:
		if p == 0:
			print(z + max(p, n), n)
		elif n == 0:
			print(z + max(p, n), p)
		else:
			print(z + max(p, n), min(p, n))
	else:
		print(z + max(p, n), 1)
