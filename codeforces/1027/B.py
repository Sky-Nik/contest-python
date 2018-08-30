def solve(x, y, n):
    if (x + y) % 2 == 0:
        return (n * (x - 1) + y + 1) // 2
    else:
        return (n ** 2 + 1) // 2 + (n * (x - 1) + y + 1) // 2


n, q = map(int, input().split())

for i in range(q):
    xi, yi = map(int, input().split())
    print(solve(xi, yi, n))
