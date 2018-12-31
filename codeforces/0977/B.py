import sys


def solve(n: int, s: str):
	A = [[0 for j in range(26)] for i in range(26)]

	for i in range(n - 1):
		A[ord(s[i]) - ord('A')][ord(s[i + 1]) - ord('A')] += 1
	
	M = 0
	for i in range(26):
		for j in range(26):
			M = max(M, A[i][j])

	for i in range(26):
		for j in range(26):
			if M == A[i][j]:
				print(chr(i + ord('A')) + chr(j + ord('A')))
				return


if __name__ == '__main__':
	n, s = int(input()), input()

	solve(n, s)
