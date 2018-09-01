n, h, a, b, k = map(int, input().split())

for i in range(k):
    ta, fa, tb, fb = map(int, input().split())
    if ta == tb:
        print(abs(fa - fb))
    elif fa < a and fb < a:
        print(abs(ta - tb) + (a - fa) + (a - fb))
    elif fa > b and fb > b:
        print(abs(ta - tb) + (fa - b) + (fb - b))
    else:
        print(abs(ta - tb) + abs(fa - fb))
