s = input()

m = 10**9 + 7

x = [1]

for c in s:
	if c == 'b' and x[-1] != 1:
		x.append(1)
	if c == 'a':
		x[-1] += 1

a = 1

for v in x:
	a *= v
	a %= m

print(a - 1)
