#!/usr/bin/env python
from collections import Counter

n, a = int(input()), list(map(int, input().split()))

v, f = Counter(a).most_common(1)[0]
print(n - f)

i = a.index(v)
for j in range(i + 1, n):
	if a[j] != v:
		print(1 if a[j] < v else 2, j + 1, j)
for j in range(i - 1, -1, -1):
	if a[j] != v:
		print(1 if a[j] < v else 2, j + 1, j + 2)
