# https://www.hackerrank.com/challenges/security-bijective-functions/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(range(1, n + 1))
values = list(map(int, input().split()))
print("YES" if sorted(values) == x else "NO")
