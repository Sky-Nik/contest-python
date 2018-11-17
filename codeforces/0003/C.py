b = [input() for _ in range(3)]

first_won = (
	any(all(b[i][j] == 'X' for i in range(3)) for j in range(3)) or
	any(all(b[j][i] == 'X' for i in range(3)) for j in range(3)) or
	all(b[i][i] == 'X' for i in range(3)) or
	all(b[i][2 - i] == 'X' for i in range(3))
)

second_won = (
	any(all(b[i][j] == '0' for i in range(3)) for j in range(3)) or
	any(all(b[j][i] == '0' for i in range(3)) for j in range(3)) or
	all(b[i][i] == '0' for i in range(3)) or
	all(b[i][2 - i] == '0' for i in range(3))
)

count_ones = sum(sum(1 if b[i][j] == 'X' else 0 for i in range(3)) for j in range(3))

count_twos = sum(sum(1 if b[i][j] == '0' else 0 for i in range(3)) for j in range(3))

count_empty = sum(sum(1 if b[i][j] == '.' else 0 for i in range(3)) for j in range(3))

moves_diff = count_ones - count_twos

legal = (moves_diff in {0, 1}) and ((not first_won) or (not second_won)) and \
	(moves_diff == 0 or not second_won) and (moves_diff == 1 or not first_won)

if legal:
	if first_won:
		print('the first player won')
	elif second_won:
		print('the second player won')
	elif count_empty == 0:
		print('draw')
	elif moves_diff == 0:
		print('first')
	else:
		print('second')
else:
	print('illegal')
