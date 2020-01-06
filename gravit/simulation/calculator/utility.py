from math import sqrt, atan

class Vector(tuple):
	"""A 2D Vector Object for Gravit. 
	   /It used to have an acceleration-vector, velocity, deplacement-vector, etc.
	"""
    def __init__(self, x, y):
    	"""Take 2 aguments : the coords of the vector x and y.
    	"""
        super().__init__((x, y))
        
    def abs(self):
    	"""Return the norm (=lenght) of the vector
    	"""
        return sqrt(self.x**2+self.y**2)
        	        
    def dir(self):
    	"""Return the direction of the vector
    	"""
        return atan(x/y)
        
    def __mult__(self, nb):
    	"""Used to mult. vector with number like float or int
    	"""
        return Vector(self.x*nb, self.y*nb)
        
class Position(tuple):
	"""A Position object which inherits from tuple but with additionnals methods.
	"""
    def __init__(self, x, y):
    	"""Take 2 args : the coords x and y
    	"""
        super().__init__((x, y))
        
    def __add__(self, other):
    	"""Used to add 2 Positions easily.
    	"""
        return Position(self[0]+other[0],
        	                self[1]+other[1])
    def to(self, other):
    	"""Take 1 argument, another Position.
    	   /Generate a Vector from self to other.
    	"""
        return Vector(other[0]-self[0], other[1]-self[1])