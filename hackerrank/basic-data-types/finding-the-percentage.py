# https://www.hackerrank.com/challenges/finding-the-percentage/problem
student_marks = {}

for _ in range(int(input())):  # n
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

print(f'{sum(student_marks[input()]) / 3:.2f}')  # query_name
