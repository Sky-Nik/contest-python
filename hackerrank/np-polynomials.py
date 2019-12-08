# https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy as np

print(np.polyval(np.poly1d(list(map(float, input().split()))), float(input())))
