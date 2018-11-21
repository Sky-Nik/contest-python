def solve(s1, s2, s3):
	


t = int(input())

for i in range(t):
	x1s, y1s, x1f, y1f = map(int, input().split())
	x2s, y2s, x2f, y2f = map(int, input().split())
	x3s, y3s, x3f, y3f = map(int, input().split())
	p1s, p1f = (x1s, y1s), (x1f, y1f)
	p2s, p2f = (x2s, y2s), (x2f, y2f)
	p3s, p3f = (x3s, y3s), (x3f, y3f)
	s1 = (p1s, p1f)
	s2 = (p2s, p2f)
	s3 = (p3s, p3f)
	solve(s1, s2, s3)
