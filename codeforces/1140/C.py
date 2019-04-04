#!/usr/bin/env python
from heapq import *

n, k = map(int, input().split())

bt = sorted(
	list(map(
		lambda _: (_[1], _[0]), 
		[tuple(map(int, input().split())) for i in range(n)]
	)),
	reverse=True
)

ans, tl, hp = 0, 0, []

for i in range(n):
	tl += bt[i][1]
	heappush(hp, bt[i][1])

	if i >= k:
		tl -= heappop(hp)

	ans = max(ans, bt[i][0] * tl)

print(ans)
       