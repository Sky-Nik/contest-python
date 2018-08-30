def solve(n, s):
    return 'YES' if all([(ord(s[i]) - ord(s[n - 1 - i])) in (-2, 0, 2) for i in range(n)]) else 'NO'


for t in range(int(input())):
    print(solve(int(input()), input()))
