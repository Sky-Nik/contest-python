# https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque

d = deque()

for _ in range(int(input())):  # N
    ln = input().split()
    cmd = ln[0]
    if len(ln) == 1:
        if cmd == "pop":
            d.pop()
        elif cmd == "popleft":
            d.popleft()
        else:
            assert False, "Not reachable"
    else:
        arg = ln[1]
        if cmd == "append":
            d.append(arg)
        elif cmd == "appendleft":
            d.appendleft(arg)
        else:
            assert False, "Not reachable"

print(*d)
