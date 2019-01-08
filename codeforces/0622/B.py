hh, mm = map(int, input().split(':'))

a = int(input())

t = (60 * hh + mm + a) % (24 * 60)

print(f'{t // 60:02}:{t % 60:02}')