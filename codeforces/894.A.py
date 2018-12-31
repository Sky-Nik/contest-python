s = input()

a, n = 0, len(s)

for i in range(n):
	if s[i] == 'Q':
		for j in range(i + 1, n):
			if s[j] == 'A':
				for k in range(j + 1, n):
					if s[k] == 'Q':
						a += 1

print(a)
