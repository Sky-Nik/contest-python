from sys import stdin

s = []

ell = stdin.read().splitlines()[2::2]

for i, li in enumerate(ell):
    l = list(map(int, li.split()))

    if len(l) == 4:
        s.append(li)

    else:
        d = dict()
        for li in l:
            if li not in d:
                d[li] = 0
            d[li] += 1

        dg2 = []
        for di in d:
            if d[di] > 1:
                dg2.append(di)
            if d[di] > 3:
                dg2.append(di)
        dg2.sort()

        r = [dg2[i + 1] / dg2[i] for i in range(len(dg2) - 1)]

        pos = r.index(min(r))

        s.append(f'{dg2[pos]} {dg2[pos]} {dg2[pos + 1]} {dg2[pos + 1]}')

print('\n'.join(s))
