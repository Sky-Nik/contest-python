def solve(n: int, b: list):
	if n == 1:
		print(0)
		return

	answer = n + 1

	diff = b[1] - b[0]

	for d in range(diff - 2, diff + 3):
		for start in range(b[0] - 1, b[0] + 2):
			pos, to_change = start, 0
			for i in range(n):
				if abs(pos - b[i]) > 1:
					to_change = n + 1
					break

				if pos != b[i]:
					to_change += 1
				
				pos += d

			answer = min(answer, to_change)

	print(-1 if answer == n + 1 else answer)


if __name__ == '__main__':
	n = int(input())

	b = list(map(int, input().split()))

	solve(n, b)
