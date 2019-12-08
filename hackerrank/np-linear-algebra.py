# https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy as np

print(round(np.linalg.det(np.matrix([list(map(float, input().split())) for _ in range(int(input()))])), 2))
