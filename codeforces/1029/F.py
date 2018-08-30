from math import sqrt

lens = [0 for _ in range(1000000)]


def solve(a, b):
    k = 0
    for i in range(1, int(sqrt(b)) + 2):
        if b % i == 0:
            lens[k] = i
            k += 1

    ans = 2 * (a + b) + 2
    x = a + b

    l = 0
    for i in range(1, int(sqrt(x)) + 2):
        if x % i == 0:
            while l + 1 < k and lens[l + 1] <= i:
                l += 1
            if b * i <= x * lens[l]:
                ans = min(ans, (i + x // i) * 2)

    return ans


a, b = map(int, input().split())
print(min(solve(a, b), solve(b, a)))
