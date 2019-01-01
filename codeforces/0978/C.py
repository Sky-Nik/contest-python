def solve(n, a, m, b):
	prefix_sums = [0 for _ in range(n + 1)]
	
	for i in range(n):
		prefix_sums[i + 1] = prefix_sums[i] + a[i]

	f = 0
	for bi in b:
		while bi > prefix_sums[f]:
			f += 1
		print(f, bi - prefix_sums[f - 1])


if __name__ == '__main__':
	n, m = map(int, input().split())

	a = list(map(int, input().split()))

	b = list(map(int, input().split()))

	solve(n, a, m, b)
