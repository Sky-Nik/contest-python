ans = 0

for d in range(1, 1999):
	for e in range(1, 1999):
		if d + e <= 1999 and d != e:
			ans += 1

print(ans)
