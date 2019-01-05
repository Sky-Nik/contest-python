n = int(input())

p = [0, 0,] + list(map(int, input().split()))

s = [0,] + list(map(int, input().split()))

d = {}

for i in range(n):
	d[p[i]] = min(d.get(p[i], 2e9), s[i])

answer, ok = 0, True

for i in range(1, n + 1):
	# print(f's[{i}] = {s[i]}')
	
	if s[i] == -1:
		# print(f's[p[{i}]] = s[{p[i]}] = {s[p[i]]}')
		s[i] = d.get(i, s[p[i]])
	
	if s[i] < s[p[i]]:
		ok = False
		break

	answer += s[i] - s[p[i]]

print(answer if ok else -1)
