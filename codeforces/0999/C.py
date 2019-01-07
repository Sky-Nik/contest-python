n, k = map(int, input().split())
s = input()
res = [True for i in range(n)]
d = 0
alpha = 'abcdefghijklmnopqrstuvwxyz'
for _alpha in alpha:
  for i in range(n):
    if d >= k:
      break
    if s[i] == _alpha:
      res[i] = False
      d += 1
  if d >= k:
    break
res_s = ''
for i in range(n):
  if res[i]:
    res_s += s[i]
print(res_s)