n = int(input())

a = list(map(int, input().split()))

print(a.count(1))

a.append(1)

l = []

for i in range(n):
	if a[i + 1] == 1:
		l.append(str(a[i]))

print(' '.join(l))
