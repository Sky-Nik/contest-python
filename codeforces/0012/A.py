a = [input().strip() for _ in range(3)]

print('YES' if all(all(a[i][j] == a[2-i][2-j] for j in range(3)) for i in range(3)) else 'NO')
