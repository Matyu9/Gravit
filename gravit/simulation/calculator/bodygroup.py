from gravit.simulation.calculator.utility import *

class BodyGroup:
	
    def __init__(self, *bodies):
        self.bodies = bodies
        
        for body in self.bodies:
            body.master = self