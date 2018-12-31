n = int(input())

print(' '.join(map(lambda _: str(_ - 1 if _ % 2 == 0 else _), map(int, input().split()))))
