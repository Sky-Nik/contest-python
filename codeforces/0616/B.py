n, m = map(int, input().split())
	
c = [list(map(int, input().split())) for i in range(n)]

print(max(min(c[i][j] for j in range(m)) for i in range(n)))
