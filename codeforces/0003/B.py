n, v = map(int, input().split())

tp = []

for i in range(n):
	ti, pi = map(int, input().split())
	tp.append((ti, pi, i + 1))

tp.sort(key=lambda _: - _[1] / _[0])  # key = carrying capacity / space taken

numbers, v_current, quality = [], 0, 0
last_ones = -2, -1
for i, tpi in enumerate(tp):  # take as much as possible
	if v_current + tpi[0] <= v:
		v_current += tpi[0]
		quality += tpi[1]
		numbers.append(tpi[2])

		if tpi[0] == 1:
			last_ones = last_ones[1], i

# print(f'last_ones={last_ones}')
# print(f'numbers={numbers}')
# print(f'v_current={v_current}')
# print(f'quality={quality}')

if v_current == v:  # try to change two lasе ones to first 2 after pre-last 1
	numbers2, v_current2, quality2 = [], 0, 0
	for i, tpi in enumerate(tp):
		if v_current2 + tpi[0] <= v and (tpi[0] != 1 or i < last_ones[0]):
			v_current2 += tpi[0]
			quality2 += tpi[1]
			numbers2.append(tpi[2])

	# print(f'numbers2={numbers2}')
	# print(f'v_current2={v_current2}')
	# print(f'quality2={quality2}')

	if quality2 > quality:  # update solution if needed
		numbers = numbers2
		quality = quality2

if v_current + 1 == v:  # try to change last 1 to first 2 after last 1
	numbers3, v_current3, quality3 = [], 0, 0
	for i, tpi in enumerate(tp):
		if v_current3 + tpi[0] <= v and (tpi[0] != 1 or i < last_ones[1]):
			v_current3 += tpi[0]
			quality3 += tpi[1]
			numbers3.append(tpi[2])

	# print(f'numbers3={numbers3}')
	# print(f'v_current3={v_current3}')
	# print(f'quality3={quality3}')

	if quality3 > quality:  # update solution if needed
		numbers = numbers3
		quality = quality3

print(quality)
print(' '.join(map(str, numbers)))
