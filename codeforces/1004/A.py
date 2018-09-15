n, d = map(int, input().split())

x = set(map(int, input().split()))

print(sum(1 if min(list(map(lambda y: abs(_ - y), x))) == d else 0 for _ in ({_ - d for _ in x} | {_ + d for _ in x})))
