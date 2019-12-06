# https://www.hackerrank.com/challenges/re-group-groups/problem
import re
m = re.search(r"([a-zA-Z\d])\1", input())
print(m.group(1) if m else -1)
