# https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

for _ in range(int(input())):  # T
    n = int(input())
    side_lengths = deque(list(map(int, input().split())))
    ground, possible = 2**32, True
    for _ in range(n):
        left, right = side_lengths[0], side_lengths[-1]
        possible &= max(left, right) <= ground
        ground = max(left, right)
        if left > right:
            side_lengths.popleft()
        else:
            side_lengths.pop()
    print ("Yes" if possible else "No")
