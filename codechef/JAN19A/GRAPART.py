T = int(input())

def dfs(v, t):
	nonlocal used

	T[t % 4].append(v)

	used[v] = True

	for u in G[v]:
		if not used[u]:
			dfs(u, t + 1)


if __name__ == '__main__':
	for Ti in range(T):
		N = int(input())

		G = [[] for _ in range(N)]

		for i in range(N - 1):
			u, v = map(int, input().split())

			u -= 1; v -= 1

			G[u].append(v); G[v].append(u)

		used = [False for _ in range(N)]

		T = [[], [], [], []]

		dfs(0, 0)

		l = list(map(len, T))

		if l[0] + l[2] == l[1] + l[3]:
			print(1, *(T[0] + T[2]), *(T[1] + T[3]), sep='\n')

		else:
			print(2)
			
			if l[0] + l[2] > l[1] + l[3]:
				if l[0] > l[2]:
					pass
				if l[0] < l[2]:
					pass
			if l[0] + l[2] < l[1] + l[3]:
				if l[1] > l[3]:
					pass
				if l[1] < l[3]:
					pass
