n = int(input())

a, b, c = n // 3, n // 3, n // 3 + n % 3

if a % 3 == 0:
	if b % 3 != 2:
		b += 1
		a -= 1
	else:
		b -= 1
		a += 1

if b % 3 == 0:
	if c % 3 != 2:
		c += 1
		b -= 1
	else:
		c -= 1
		b += 1

if c % 3 == 0:
	if a % 3 != 2:
		a += 1
		c -= 1
	else:
		a -= 1
		c += 1

print(a, b, c)
