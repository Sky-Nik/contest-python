def signum(x):
	return (x > 0) - (x < 0)


res = sum(signum(mci[0] - mci[1]) for mci in [tuple(map(int, input().split())) for _ in range(int(input()))])

if res > 0:
	print('Mishka')
elif res < 0:
	print('Chris')
else:
	print('Friendship is magic!^^')
