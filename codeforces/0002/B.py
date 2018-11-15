def h(x, m):
    i = 0
    
    while x % m == 0:
        i += 1
        x //= m
        
    return i


n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]  # revert 10s back

a10 = [[a[i][j] if a[i][j] != 0 else 10 for j in range(n)] for i in range(n)]

a2 = [[h(a10[i][j], 2) for j in range(n)] for i in range(n)]

a5 = [[h(a10[i][j], 5) for j in range(n)] for i in range(n)]

dp2 = [[-1 for _ in range(n)] for _ in range(n)]

dp5 = [[-1 for _ in range(n)] for _ in range(n)]


def d2(r, c):
    if dp2[r][c] != -1:
        return dp2[r][c]
    
    if r == 0:
        if c == 0:
            dp2[0][0] = a2[0][0]
        else:
            dp2[0][c] = dp2[0][c - 1] + a2[0][c]
    elif c == 0:
        dp2[r][0] = dp2[r - 1][0] + a2[r][0]
    else:
        dp2[r][c] = min(dp2[r - 1][c], dp2[r][c - 1]) + a2[r][c]
    
    return dp2[r][c]


def d5(r, c):
    if dp5[r][c] != -1:
        return dp5[r][c]

    if r == 0:
        if c == 0:
            dp5[0][0] = a5[0][0]
        else:
            dp5[0][c] = dp5[0][c - 1] + a5[0][c]
    elif c == 0:
        dp5[r][0] = dp5[r - 1][0] + a5[r][0]
    else:
        dp5[r][c] = min(dp5[r - 1][c], dp5[r][c - 1]) + a5[r][c]

    return dp5[r][c]

