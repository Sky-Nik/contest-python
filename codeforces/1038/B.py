n = int(input())
if n < 3:
    print('No')
else:
    print('Yes')
    if n % 2 == 0:
        print(1, n // 2)
        print(n - 1, *([i for i in range(1, n // 2)] + [i for i in range(n // 2 + 1, n + 1)]))
    else:
        print(1, n)
        print(n - 1, *[i for i in range(1, n)])
