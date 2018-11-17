def step():
	global x1, x2, y1, y2, step_count, moves

	move = ''
	
	if x1 > x2:
		move += 'L'
		x1 -= 1
	elif x1 < x2:
		move += 'R'
		x1 += 1

	if y1 > y2:
		move += 'D'
		y1 -= 1
	elif y1 < y2:
		move += 'U'
		y1 += 1

	step_count += 1

	moves.append(move)


if __name__ == '__main__':
	p1 = input()
	x1, y1 = ord(p1[0]) - ord('a'), int(p1[1])

	p2 = input()
	x2, y2 = ord(p2[0]) - ord('a'), int(p2[1])

	step_count, moves = 0, []

	while x1 != x2 or y1 != y2:
		step()

	print(step_count)

	print('\n'.join(moves))
