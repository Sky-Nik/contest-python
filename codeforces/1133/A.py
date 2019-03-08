h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

M1 = 60 * h1 + m1
M2 = 60 * h2 + m2

M = (M1 + M2) // 2

h, m = M // 60, M % 60

print(f'{h:02}:{m:02}')