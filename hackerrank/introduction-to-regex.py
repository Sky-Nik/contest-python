# https://www.hackerrank.com/challenges/introduction-to-regex/problem
for _ in range(int(input())):  # T
    s = input()
    try:
        float(s)
        print('.' in s)
    except:
        print(False)
