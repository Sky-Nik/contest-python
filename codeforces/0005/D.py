from math import sqrt

a, v = map(int, input().split())
l, d, w = map(int, input().split())

if v <= w:
	print('on line 7')
	t = v / a  # time needed to get maximum possible velocity
	s = a * t**2 / 2  # path travelled while getting maximum velocity
	if s <= l:  # car reaches max velocity and rides on it for a while
		print('on line 11')
		t2 = (l - s) / v  # remaining time
		print(f't = {t}, t2 = {t2}', t + t2)
	else:  # car reaches Berkuver defore reaching max velocity
		print('on line 15')
		t = sqrt(2 * l / a)  # time to reach Berkuver
		print(f't = {t}', t)
else:
	print('on line 19')
	t = w / a  # time to reach speed limit
	s = a * t**2 / 2  # path travelled before reaching speed limit
	if s <= d:
		print('on line 23')
		t2 = 2 * (v - w) / a  # time to reach max velocity and slow down bak
		s2 = a * t2**2 + 2 * t2 * w  # path travelled while reaching max velocity and sloцing down back
		if s + s2 <= d:
			print('on line 27')
			t3 = (d - s - s2) / v  # time at the max velocity
			t4 = (l - d) / w  # remaining time
			print(f't = {t}, t2 = {t2}, t3 = {t3}, t4 = {t4}', t + t2 + t3 + t4)
		else:
			print('on line 32')
			t2 = 2 * (sqrt(w**2 + a * d - a * s) - w) / a
			t3 = (l - d) / w  # remaining time
			print(f't = {t}, t2 = {t2}, t3 = {t3}', t + t2 + t3) 
	elif s <= l:  # car reaches speed limit after sign and before Berkuver
		print('on line 37')
		t2 = (l - s) / w  # remaining time
		print(f't = {t}, t2 = {t2}', t + t2)
	else:  # car reaches Berkuver before reaching speed limit
		print('on line 41')
		t = sqrt(2 * l / a)  # time to reach Berkuver
		print(f't = {t}', t)
