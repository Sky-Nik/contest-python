x, y, z, t1, t2, t3 = map(int, input().split())

li, le = (abs(z - x) + abs(x - y)) * t2 + 3 * t3, abs(x - y) * t1

print('YES' if li <= le else 'NO')
