from math import sqrt, atan

class Vector(tuple):

    def __init__(self, x, y):
        super().__init__((x, y))

    def abs(self):
        return sqrt(self.x**2+self.y**2)

    def dir(self):
        return atan(x/y)

    def __add__(self, other):
        return Vector(self[0]+other[0], self[1]+other[1])

    def __mult__(self, nb):
        return Vector(self[0]*nb, self[1]*nb)

class Position(tuple):
    def __init__(self, x, y):
        super().__init__((x, y))

    def __add__(self, other):
        return Position(self[0]+other[0],
                        self[1]+other[1])
    def to(self, other):
        return Vector(other[0]-self[0], other[1]-self[1])
