d = {
	'purple': 'Power',
	'green': 'Time',
	'blue': 'Space',
	'orange': 'Soul',
	'red': 'Reality',
	'yellow': 'Mind'
}

n = int(input())

for _ in range(n):
	del d[input()]

print(len(d))

print('\n'.join(d.values()))
