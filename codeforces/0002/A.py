scores = {}
queue = []

for _ in range(int(input())):
    name, score = input().split()
    queue.append((name, score))
    scores[name] = scores.get(name, 0) + int(score)

m = max(scores.values())

names = set(filter(lambda _: scores[_] == m, scores.keys()))  # side comment: without a set() it won't work

scores = {}

for name, score in queue:
    scores[name] = scores.get(name, 0) + int(score)
    if scores[name] >= m and name in names:
        print(name)
        break
