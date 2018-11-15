import re


def solve(string):
    if re.match(r"R\d+C\d+", string):
        row_int, col_int = map(int, string.replace('R', '').split('C'))
        power, length = 1, 0

        while col_int >= power:
            col_int -= power
            power *= 26
            length += 1

        col_str = ''
        for _ in range(length):
            col_str = chr(ord('A') + col_int % 26) + col_str
            col_int //= 26

        print(f'{col_str}{row_int}')

    else:
        row_str, col_str = '', ''
        for _ in range(len(string)):
            if string[_].isalpha():
                col_str += string[_]
            else:
                row_str += string[_]

        col_int = 0
        for _ in col_str:
            col_int *= 26
            col_int += ord(_) - ord('A')
        for _ in range(len(col_str)):
            col_int += 26**_

        print(f'R{row_str}C{col_int}')


for _ in range(int(input())):
    solve(input())
