d, sumTime = map(int, input().split())

minTime, maxTime = [None for _ in range(d)], [None for _ in range(d)]

for i in range(d):
	minTime[i], maxTime[i] = map(int, input().split())

answer = [None for _ in range(d)]

for i in range(d):
	sumTime -= minTime[i]
	answer[i] = minTime[i]
	maxTime[i] -= minTime[i]
	minTime[i] = 0

for i in range(d):
	if sumTime > 0:
		timeSpend = min(sumTime, maxTime[i])
		sumTime -= timeSpend
		answer[i] += timeSpend
		maxTime[i] -= timeSpend

if sumTime == 0:
	print('YES')
	print(' '.join(map(str, answer)))
else:
	print('NO')
