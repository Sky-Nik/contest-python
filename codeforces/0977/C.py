def solve(n: int, k: int, A: list):
	A.sort()
	
	if k == 0 and A[0] == 1:
		print(-1)
	elif k == 0 and A[0] > 1:
		print(1)
	elif n == k:
		print(1000000000)
	elif A[k] > A[k - 1]:
		print(A[k - 1])
	else:
		print(-1)


if __name__ == '__main__':
	n, k = map(int, input().split())

	A = list(map(int, input().split()))

	solve(n, k, A);
