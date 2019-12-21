# https://www.hackerrank.com/challenges/security-tutorial-permutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
f = list(map(int, input().split()))
print("\n".join(map(str, [f[f[i] - 1] for i in range(n)])))
