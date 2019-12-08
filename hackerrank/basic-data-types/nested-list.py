# https://www.hackerrank.com/challenges/nested-list/problem
m = {}

for _ in range(int(input())):  # n
    name, score = input(), float(input())
    if score not in m:
        m[score] = []
    m[score].append(name)

print('\n'.join(sorted(sorted(m.items())[1][1])))
