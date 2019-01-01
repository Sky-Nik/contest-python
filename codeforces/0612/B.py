def solve(n: int, f: list):
	index_f = [(f[i], i) for i in range(n)]

	index_f.sort()

	answer = 0
	for i in range(n - 1):
		answer += abs(index_f[i][1] - index_f[i + 1][1])

	print(answer)


if __name__ == '__main__':
	n = int(input())

	f = list(map(int, input().split()))

	solve(n, f)
