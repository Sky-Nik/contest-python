n = int(input())

rounds = []

for i in range(n):
	name, score = input().split()

	score = int(score)

	rounds.append((name, score))

a = {}

for name, score in rounds:
	a[name] = a.get(name, 0) + score

m = max(a.values())

