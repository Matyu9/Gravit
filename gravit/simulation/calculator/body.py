from .utility import *
from pygame.time import Clock

G = 6.67430*(10**-11)

class Body:
	"""Math-only object which calc. the body deplacement.'"""
    def __init__(self, mass, pos):
        self.mass = mass #mass is a float
        self.pos = pos # pos is a Position object
        self.acceleration = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.deplacement = Vector(0, 0)
        self.master = master
