import threading
import time


from body import *

## Constantes de la Physique
G = 6.6743015*(10**-11)# SI


class Calculator(threading.Thread):

	def do_play(self):
		self.play = True
		self.stop = False

	def do_pause(self):
		self.play = False
		self.stop = False

	def do_stop(self):
		self.play = False
		self.stop = True

	def __init__(self, *bodies, TPS=100):
		super().__init__()
		self.bodies = BodyList()
		for b in bodies:
			self.bodies.append(b)
		self.max_tps = TPS
		self.TPS = TPS

	def calc_move(self, body):

		body.acceleration = Vector(0, 0)
		for other in self.bodies-BodyList(body):
			a = (body.pos.to(other.pos))
			b = (other.mass / (body.pos.to(other.pos).abs()**3))
			body.acceleration += a * b

		body.acceleration *= -G

		body.velocity = body.acceleration*self.TPS
		body.velocity += body.inertia

		body.deplacement = body.velocity*self.TPS

		return body.deplacement

	def run(self):
		self.do_play()
		while not self.stop:
			while self.play:
				t = time.time()
				for body in self.bodies:
					body.move(self.calc_move(body))
				time.sleep(1/self.max_tps-(time.time()-t))


if __name__=="__main__":

	c = Calculator(
					Body("obj1", 10**12, Position(0.0, 0.0)),
					Body("obj2", 10**12, Position(1000.0, 0.0)))

	c.start()
