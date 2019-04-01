#!/usr/bin/env python

n, a = int(input()), list(map(int, input().split()))

o, e = sorted(list(filter(lambda _: _ & 1, a))), \
	sorted(list(filter(lambda _: not (_ & 1), a)))

idx = min(len(o), len(e))

print(sum(o[:-1-idx]) + sum(e[:-1-idx]))
