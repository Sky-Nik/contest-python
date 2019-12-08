# https://www.hackerrank.com/challenges/re-start-re-end/problem
import re
s, k, f = input(), input(), 0
if k in s:
    while f < len(s) and k in s[f:]:
        m = re.search(k, s[f:])
        print(f"({f + m.start()}, {f + m.end() - 1})")
        f += m.start() + 1
else:
    print("(-1, -1)")
