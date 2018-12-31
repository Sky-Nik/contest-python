def solve(n: int, k: int):
	for i in range(k):
		if n % 10 != 0: 
			n -= 1
		else:
			n //= 10

	print(n)


if __name__ == '__main__':
	n, k = map(int, input().split())

	solve(n, k)
