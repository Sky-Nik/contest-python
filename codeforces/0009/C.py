n = int(input())

print(len(set(filter(lambda _: _ <= n, {int(bin(_)[2:]) for _ in range(1, 2**10 + 1)}))))
