# hackerrank.com/challenges/python-lists/problem
l = []

for _ in range(int(input())):
    cmd, *args = input().split()
    if cmd == 'insert':
        i, e = map(int, args)
        l.insert(i, e)
    if cmd == 'print':
        print(l)
    if cmd == 'remove':
        l.remove(int(args[0]))
    if cmd == 'append':
        l.append(int(args[0]))
    if cmd == 'sort':
        l.sort()
    if cmd == 'pop':
        l.pop()
    if cmd == 'reverse':
        l.reverse()
