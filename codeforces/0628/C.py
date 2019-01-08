n, k = map(int, input().split())

s = list(input())


def dist(a, b):
	return abs(ord(a) - ord(b))


for i in range(n):
	if k > 0:
		dz, da = dist(s[i], 'z'), dist(s[i], 'a')
		if dz > da:
			s[i] = chr(min(ord('z'), ord(s[i]) + k))
			k -= dz
		else:
			s[i] = chr(max(ord('a'), ord(s[i]) - k))
			k -= da

print(-1 if k > 0 else ''.join(s))
