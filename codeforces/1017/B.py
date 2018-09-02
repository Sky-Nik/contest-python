n, a, b = int(input()), input(), input()

oo = sum(a[i] == '0' and b[i] == '0' for i in range(n))
ol = sum(a[i] == '0' and b[i] == '1' for i in range(n))
lo = sum(a[i] == '1' and b[i] == '0' for i in range(n))
ll = sum(a[i] == '1' and b[i] == '1' for i in range(n))

print(oo * lo + ll * oo + lo * ol)
