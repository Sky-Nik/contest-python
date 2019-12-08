# https://www.hackerrank.com/challenges/incorrect-regex/problem
import re
for _ in range(int(input())):  # T
    try:
        re.compile(input())
        print(True)
    except:
        print(False)
