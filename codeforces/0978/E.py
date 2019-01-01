def solve(n: int, w: int, a: list):
	low, now, high = 0, 0, 0
	for ai in a:
		now += ai
		low, high = min(low, now), max(high, now)

	print(w + 1 + low - high if high - low <= w else 0)
	

if __name__ == '__main__':
	n, w = map(int, input().split())
	
	a = list(map(int, input().split()))

	solve(n, w, a)
