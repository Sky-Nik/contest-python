n = int(input())
a = list(map(int, input().split()))
ans = []
l, s = 0, set()
for i in range(n):
	if a[i] in s:
		ans.append([l+1,i+1])
		l = i + 1
		s = set()
	else:
		s.add(a[i])
if not ans:
	print(-1)
else:
	ans[-1][1] = n
	print(len(ans))
	for ansi in ans:
		print(*ansi)
