def solve(s: str):
	stack = []

	answer = 0

	for c in s:
		if c in '([{<':
			stack.append(c)
		else:
			if not stack:
				print("Impossible")
				return

			b = stack[-1]
			if b == '(' and c != ')' or b == '[' and c != ']' or \
				b == '{' and c != '}' or b == '<' and c != '>':
				answer += 1;

			stack.pop()

	print("Impossible" if stack else answer)


if __name__ == '__main__':
	s = input()

	solve(s)
