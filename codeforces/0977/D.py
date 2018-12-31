def exp_3(a: int) -> int:
	ans = 0
	
	while a % 3 == 0:
		a //= 3
		ans += 1

	return ans


def exp_2(a: int) -> int:
	ans = 0

	while a % 2 == 0:
		a //= 2
		ans += 1

	return ans


def comp(a: int, b: int) -> bool:
	if exp_3(a) > exp_3(b):
		return -1
	elif exp_3(a) < exp_3(b):
		return 1
	elif exp_2(a) < exp_2(b):
		return -1
	else:
		return 1


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def solve(n: int, A: list):
	print(' '.join(list(map(str, sorted(A, key=cmp_to_key(comp))))))
	

if __name__ == '__main__':
	n = int(input())
	
	A = list(map(int, input().split()))

	solve(n, A)
