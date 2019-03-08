n = int(input())

a = list(map(int, input().split()))

a.sort()

a.append(a[-1] + 6)

i, j = 0, 0

ans = 0

while i < n and j < n + 1:
	while a[i] + 5 >= a[j]:
		j += 1

	ans = max(ans, j - i)

	i += 1

print(ans)