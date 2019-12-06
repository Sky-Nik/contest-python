# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
import math


class Points:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x; self.y = y; self.z = z

    def __sub__(self, other: 'Points') -> 'Points':
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other: 'Points') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: 'Points') -> 'Points':
        return Points(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )
        
    def absolute(self) -> float:
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    Pointss = list()
    for i in range(4):
        a = list(map(float, input().split()))
        Pointss.append(a)

    a, b, c, d = Pointss(*Pointss[0]), Pointss(*Pointss[1]), Pointss(*Pointss[2]), Pointss(*Pointss[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
