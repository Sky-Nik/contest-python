n = int(input())

l = [(-sum(map(int, input().split())), i) for i in range(n)]

TomasSmith = l[0]

l.sort()

print(l.index(TomasSmith) + 1)
