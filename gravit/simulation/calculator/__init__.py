import threading
import time
import math


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

    def __init__(self, *bodies, TPS=0.5):
        super().__init__()
        self.bodies = BodyList()
        for b in bodies:
            self.bodies.append(b)
        self.max_tps = TPS
        self.TPS = TPS

    def calculate_acceleration(self):
        a = len(self.bodies) - 1
        while a >= 0:
            objectA = self.bodies[a]
            # Calculate forces applied to objects
            b = len(self.bodies) - 1
            while b >= 0:
                if b != a:
                    objectB = self.bodies[b] ## OutOfRange : pb de
                    # Calculate the distance between objectA and objectB
                    distance = objectA.pos.to(objectB.pos).abs()

                    # Find angle from vector. Fun note, if we reverse objectA and B we have anti-gravity
                    angleToMass = math.atan2(
                        objectB.pos[1]-objectA.pos[1],
                        objectB.pos[0]-objectA.pos[0]
                    )
                    # All credit for this formula goes to an Isaac Newton
                    objectA.acceleration += (
                        math.cos(angleToMass) *
                        (objectB.mass/distance**2), # velocity X
                        math.sin(angleToMass) *
                        (objectB.mass/distance**2) # velocity Y
                    )
                b -=1
            a -= 1

    # Loops through all objects and applies the force delta to the velocity
    def apply_acceleration(self):
        for body in self.bodies:

            body.velocity += (body.acceleration[0] * self.TPS,
                              body.acceleration[1] * self.TPS)

            body.move((body.velocity[0] * self.TPS * -G,
                      body.velocity[1] * self.TPS * -G
            ))
            # Reset body acceleration
            body.acceleration = Vector(0, 0)

    """def calc_move(self, body):

        body.acceleration = Vector(0, 0) # ->aM =
        for other in self.bodies-BodyList(body): # ∑ (
            a = (body.pos.to(other.pos)) # Pi->PM
            b = (other.mass / ((body.pos.to(other.pos).abs())**3)) # mi /( ||Pi->PM||^3 )
            body.acceleration += a * b # mi /( ||Pi->PM||^3 ) * Pi->PM

        body.acceleration *= -G

        body.velocity = body.acceleration*self.TPS
        body.velocity += body.inertia

        body.deplacement = body.velocity*self.TPS

        return body.deplacement"""

    def run(self):
        self.do_play()
        while not self.stop:
            for body in self.bodies:
                body.move(Vector(0, 0))
            time.sleep(1/self.max_tps)
            while self.play:
                t = time.time()
                self.calculate_acceleration()
                self.apply_acceleration()
                time.sleep(1/self.max_tps)


if __name__=="__main__":

    c = Calculator(
                    Body("obj1", 6*(10**24), Position(-10000, 0)),
                    Body("obj2", 6*(10**24), Position(10000, 0))
    ) # simulation qui montre 2 terres à 20'000 kms l'une de l'autre

    c.start() 
