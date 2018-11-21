import re

ab, s1, s2 = input(), input(), input()

f, b = re.search(fr'.*{s1}.*{s2}.*', ab), re.search(fr'.*{s2[::-1]}.*{s1[::-1]}.*', ab)

if f:
	if b:
		print('both')
	else:
		print('forward')
else:
	if b:
		print('backward')
	else:
		print('fantasy')
