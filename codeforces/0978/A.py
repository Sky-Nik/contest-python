n = int(input())

a = list(map(int, input().split()))

s, f = set(), []

for i in range(n)[::-1]:
	if a[i] not in s:
		s.add(a[i])
		f.append(str(a[i]))

print(len(f))

print(' '.join(f[::-1]))
