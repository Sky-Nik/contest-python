def solve(n):
	if n == '0':
		return '0'

	s = ''.join(sorted(n))
	pos = min(filter(lambda _: s[_] != '0', range(len(s))))
	return s[pos] + s[:pos] + s[pos + 1:]


n, m = input().strip(), input().strip()

print('OK' if m == solve(n) else 'WRONG_ANSWER')
