from gravit.simulation.calculator.utility import *
from pygame.time import Clock

G = 6.67430*(10**-11)

class Body:
	"""Math-only object which calc. the body deplacement.'"""
    def __init__(self, mass, pos):
        self.mass = mass #mass is a float
        self.pos = pos # pos is a Position object
        self.acceleration = Vector(0, 0)
        self.master = None
    def calc_move(self):
        if self.master != None or self in self.master.bodies:
            a = 0
            for i in self.master.bodies:
                a += self.mass*i.mass/(i.pos.to(self.pos).abs()**3)*i.pos.to(self.pos)
            
            self.acceleration = -G * a
