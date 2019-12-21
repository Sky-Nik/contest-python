# https://www.hackerrank.com/challenges/security-key-spaces/problem
m, e = list(input()), int(input())
print(''.join(map(lambda c: str((int(c) + e) % 10), m)))
