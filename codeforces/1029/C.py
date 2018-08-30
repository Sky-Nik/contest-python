def intersect(a, b):
    return max(a[0], b[0]), min(a[1], b[1])


def length(a):
    return max(a[1] - a[0], 0)


n = int(input())

segments = []

for i in range(n):
    left, right = input().split()
    segments.append((int(left), int(right)))

pre, suf = [(0, 10**9)], [(0, 10**9)]

for i in range(0, n - 1):
    pre.append(intersect(pre[-1], segments[i]))
    suf.append(intersect(suf[-1], segments[n - 1 - i]))

print(max([length(intersect(pre[i], suf[n - 1 - i])) for i in range(n)]))
