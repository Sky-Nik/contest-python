# https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]

print(max(sum(xi**2 for xi in xis) % m for xis in product(*lists)))
