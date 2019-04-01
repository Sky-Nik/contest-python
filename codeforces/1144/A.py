#!/usr/bin/env python

for _ in range(int(input())):
	s = input()

	f = [0 for _ in range(26)]

	for c in s:
		f[ord(c) - ord('a')] += 1

	ok = False

	for i in range(26):
		for j in range(i, 26):
			_ok = True
			for k in range(26):
				if f[k] != (1 if (i <= k <= j) else 0):
					_ok = False
			if _ok:
				ok = True

	print('Yes' if ok else 'No')
