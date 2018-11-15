from math import sin, atan2, pi, sqrt

ax, ay = map(float, input().split())
bx, by = map(float, input().split())
cx, cy = map(float, input().split())

cmx, cmy = (ax + bx) / 2, (ay + by) / 2
bmx, bmy = (ax + cx) / 2, (ay + cy) / 2

cgx, cgy = bx - ax, by - ay
bgx, bgy = cx - ax, cy - ay

cpgx, cpgy = cgy, - cgx
bpgx, bpgy = bgy, - bgx

ox, oy = (cpgy * (bpgy * bmy - bpgx * bmx) - bpgy * (cpgy * cmy - cpgx * cmx)) / (- cpgy * bpgx + cpgx * bpgy), \
         (- bpgx * (cpgy * cmy - cpgx * cmx) + cpgx * (bpgy * bmy - bpgx * bmx)) / (- cpgy * bpgx + cpgx * bpgy)

oaa, oba, oca = atan2(ay - oy, ax - ox), atan2(by - oy, bx - ox), atan2(cy - oy, cx - ox)

for n in range(3, 101):
    if (
        abs(sin(n * (oaa - oba) / 2)) < 1e-4 and
        abs(sin(n * (oaa - oca) / 2)) < 1e-4 and
        abs(sin(n * (oba - oca) / 2)) < 1e-4
    ):
        print(n / 2 * sin(2 * pi / n) * ((ox - ax)**2 + (oy - ay)**2))

        break

# TODO: fix
