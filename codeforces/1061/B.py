n, m = map(int, input().split())

a = list(map(int, input().split()))

a.sort(reverse=True)

a.append(0)

j, s = a[0], 0

for i in range(n):
	if j > 0:
		if j - 1 <= a[i + 1] and j - 1 > 0:
			j -= 1
			s += 1
		elif j - 1 > a[i + 1]:
			s += j - a[i + 1]
			j = a[i + 1]
		elif a[i + 1] > 0:
			j = 1
			s += 1
		elif a [i + 1] == 0:
			j = 0
			s += 1
			break
	else:
		break

print(sum(a) - s)
