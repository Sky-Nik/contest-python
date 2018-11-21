minH, maxH = 1, 1e6

n, k = map(int, input().split())
h = list(map(int, input().split()))

minTree = [maxH + 1 for _ in range(4 * n)]
maxTree = [minH - 1 for _ in range(4 * n)]


def buildMinTree(v, tl, tr):
	if tl == tr:
		minTree[v] = h[tl]

	else:
		tm = (tl + tr) // 2
		buildMinTree(2 * v, tl, tm)
		buildMinTree(2 * v + 1, tm + 1, tr)
		minTree[v] = min(minTree[2 * v], minTree[2 * v + 1])


def buildMaxTree(v, tl, tr):
	if tl == tr:
		maxTree[v] = h[tl]

	else:
		tm = (tl + tr) // 2
		buildMaxTree(2 * v, tl, tm)
		buildMaxTree(2 * v + 1, tm + 1, tr)
		maxTree[v] = max(maxTree[2 * v], maxTree[2 * v + 1])


buildMinTree(1, 0, n - 1)
buildMaxTree(1, 0, n - 1)


def findMinTree(v, tl, tr, l, r):
	if l > r:
		return maxH + 1
	
	if l == tl and r == tr:
		return minTree[v]
	
	tm = (tl + tr) // 2
	
	return min(
		findMinTree(2 * v, tl, tm, l, min(tm, r)), 
		findMinTree(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
	)


def findMaxTree(v, tl, tr, l, r):
	if l > r:
		return minH - 1
	
	if l == tl and r == tr:
		return maxTree[v]
	
	tm = (tl + tr) // 2
	
	return max(
		findMaxTree(2 * v, tl, tm, l, min(tm, r)), 
		findMaxTree(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
	)


def binaryFind(L, l, r):
	if l + 1 == r:
		return l

	m = (l + r) // 2

	if findMaxTree(1, 0, n - 1, L, m) - findMinTree(1, 0, n - 1, L, m) <= k:
		return binaryFind(L, m, r)

	else:
		return binaryFind(L, l, m)


a, b, p = -1, 0, []

for l in range(n):
	r = binaryFind(l, l, n)

	if r - l > a:
		a, b, p = r - l, 1, [(l, r)]

	elif r - l == a:
		b += 1
		p.append((l, r))

print(a + 1, b)

for pl, pr in p:
	print(pl + 1, pr + 1)
