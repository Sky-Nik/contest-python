def gcd(x, y):
	while y != 0:
		x, y = y, x % y
	return x


def lcm(x, y):
	return (x * y) // gcd(x, y)

 
n, m, z = map(int, input().split())

print(z // lcm(n, m))
