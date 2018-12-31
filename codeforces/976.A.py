n = int(input())

s = input()

print(('1' + '0' * s.count('0')) if s != '0' else '0')
