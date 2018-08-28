def avg(collection):
    collection = list(collection)
    return sum(collection) // len(collection)


n, m = map(int, input().split())
A = [input() for i in range(n)]
rows_with_black = filter(lambda i: 'B' in A[i], range(n))
cols_with_black = filter(lambda j: 'B' in (A[i][j] for i in range(n)), range(m))
print(avg(rows_with_black) + 1, avg(cols_with_black) + 1)
