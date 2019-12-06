# https://www.hackerrank.com/challenges/any-or-all/problem
n = int(input())
a = input().split()
print(all(map(lambda x: int(x) > 0, a)) and any(map(lambda x: x[::-1] == x, a)))
