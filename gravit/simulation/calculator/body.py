from utility import *

class Body:
    def __init__(self, name, mass, pos):
        self.name = name
        self.mass = mass #mass is a float
        self.pos = pos # pos is a Position object
        self.acceleration = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.deplacement = Vector(0, 0)
        self.master = 0
        self.inertia = Vector(0, 0)
    
    def move(self, pos):
        self.pos += pos
        print( self.name + "'s pos : (" + str(self.pos[0]) + ", " + str(self.pos[1])+ ")" )
