n = int(input())
a = list(map(int, input().split()))
if any(ai % 2 == 0 for ai in a) and any(ai % 2 == 1 for ai in a):
    print(*sorted(a))
else:
    print(*a)
