# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
_ = int(input())
print(sorted(list(set(map(int, input().split()))))[-2])  # a
