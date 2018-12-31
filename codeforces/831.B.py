f, t, w = input(), input(), input()

dl = {f[_].lower(): t[_].lower() for _ in range(len(f))}
du = {f[_].upper(): t[_].upper() for _ in range(len(f))}

r = ''
for i in range(len(w)):
	if w[i] in dl:
		r += dl[w[i]]
	elif w[i] in du:
		r += du[w[i]]
	else:
		r += w[i]
print(r)
