n = int(input())

s = 'S' + input().strip() + 'S'

L, R, G = [], [], 0

for i in range(n + 1):
	if s[i] == 'G':
		G += 1
	if s[i] == 'S' and s[i + 1] == 'G':
		L.append(i + 1)
	if s[i] == 'G' and s[i + 1] == 'S':
		R.append(i)

M = 0

for i in range(len(L)):
	if G > R[i] - L[i] + 1:
		M = max(M, R[i] - L[i] + 2)
	else:
		M = max(M, R[i] - L[i] + 1)

for i in range(len(L) - 1):
	if L[i + 1] == R[i] + 2:
		if G > R[i + 1] - L[i]:
			M = max(M, R[i + 1] - L[i] + 1)
		else:
			M = max(M, R[i + 1] - L[i])

print(M)
