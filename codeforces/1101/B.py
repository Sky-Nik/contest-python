import sys

s = input()

n = len(s)

ans = ""

p1, p2, p3, p4 = None, None, None, None

for i in range(n):
	if s[i] == '[' and p1 is None:
		p1 = i
	if s[i] == ':' and p1 is not None and p2 is None:
		p2 = i

for i in range(n - 1, -1, -1):
	if s[i] == ']' and p4 is None:
		p4 = i
	if s[i] == ':' and p4 is not None and p3 is None:
		p3 = i

if p2 >= p3:
	print(-1)
	sys.exit(0)

ans = 4 

for i in range(p2, p3):
	if s[i] == '|':
		ans += 1

print(ans)
