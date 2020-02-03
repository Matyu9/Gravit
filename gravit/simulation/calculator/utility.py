from math import sqrt, atan

class Vector(tuple):

    def __new__(cls, x, y):
        self = super().__new__(cls, (x, y))
        return self

    def abs(self):
        
        return sqrt(self[0]**2+self[1]**2)

    def dir(self):
        
        return atan(self[0]/self[1])

    def __add__(self, other):
        
        return Vector(self[0]+other[0], self[1]+other[1])

    def __mul__(self, nb):
        
        return Vector(self[0]*nb, self[1]*nb)

    def __repr__(self):
        
        return "Vector("+str(self[0])+", "+str(self[1])+")"

class Position(tuple):

    def __new__(cls, x, y):
        self = super().__new__(cls, (x, y))
        return self

    def __add__(self, other):
        return Position(self[0]+other[0],
                        self[1]+other[1])


    def to(self, other):
        return Vector(other[0]-self[0], other[1]-self[1])

    def __repr__(self):
        return "Position("+str(self[0])+", "+str(self[1])+")"

class BodyList(list):
    def __init__(self, *args):
        super().__init__(args)

    def __sub__(self, other):
        n = BodyList()
        for i in self:
            if not i in other:
                n.append(i)
        return n
