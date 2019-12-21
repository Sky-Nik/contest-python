# https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
f = list(map(int, input().split()))
g = [None for _ in range(n)]
for i, fi in enumerate(f):
    g[fi - 1] = i + 1
print("\n".join(map(str, g)))
