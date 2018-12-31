n = int(input())

f = input()

while f.count('xxx') > 0:
	f = f.replace('xxx', 'xx')

print(n - len(f))
