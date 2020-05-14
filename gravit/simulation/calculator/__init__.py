import threading
import time
import math

class Body:
    def __init__(self, name, mass, pos, acceleration=[0, 0], velocity=[0, 0]):
        self.name = name
        self.m = mass  # mass is the mass of that object
        self.pos = pos  # pos is a list of x and y position of that body in pixels eg : [500,600]
        self.a = acceleration  # acceleration is a list of x and y components of accelaration of that body in pixel units
        self.v = velocity  # velocity is a list of x and y components of velocity of that body in pixel units


## Constantes de la Physique
G = 1 # SI


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

    def __init__(self, *bodies, TPS=15, delta=None):
        super().__init__()
        self.bodies = []
        for b in bodies:
            self.bodies.append(b)
        self.time = 0.0
        self.max_tps = TPS
        if delta == None:
            self.delta = 1/self.max_tps
        else:
            self.delta = delta

    def calculate_forces(self, pos_a, pos_b, m_a, m_b):
        x_diff = pos_b[0] - pos_a[0]
        y_diff = pos_b[1] - pos_a[1]
        hypotenuse = math.sqrt(((x_diff) ** 2 + (y_diff) ** 2))
        sin = x_diff / hypotenuse
        cos = y_diff / hypotenuse
        f = G * m_a * m_b / hypotenuse ** 2
        fx = f * sin
        fy = f * cos

        return fx, fy

    def apply_forces(self):
        in_t = time.time()

        for body_a in self.bodies:
            pos_a = body_a.pos
            m_a = body_a.m
            fx_total = 0
            fy_total = 0

            for body_b in self.bodies:
                if body_b.pos == pos_a:
                    continue
                fx, fy = self.calculate_forces(pos_a, body_b.pos, m_a, body_b.m)
                fx_total += fx
                fy_total += fy

            body_a_acceleration = body_a.a

            body_a_acceleration[0] = fx_total / m_a
            body_a_acceleration[1] = fy_total / m_a

            body_a.v[0] = body_a.v[0] + body_a_acceleration[0] * self.delta
            body_a.v[1] = body_a.v[1] + body_a_acceleration[1] * self.delta

            pos_a[0] = 0.5 * body_a_acceleration[0] * self.delta * self.delta + body_a.v[0] * self.delta + pos_a[0]
            pos_a[1] = 0.5 * body_a_acceleration[1] * self.delta * self.delta + body_a.v[1] * self.delta + pos_a[1]

            # Infos de debug
            # if __name__=="__main__":
            #     print("[{}] : ({}, {})".format(body_a.name, pos_a[0], pos_a[1]))

        self.run_speed = time.time() - in_t

    def run(self):
        t = 0.0
        self.do_play()
        while not self.stop:
            while self.play:
                self.apply_forces()
                self.TPS = 1/(self.max_tps)-self.run_speed
                time.sleep(1/self.max_tps)



if __name__=="__main__":

    c = Calculator(
                    Body("obj1", 10**6, [-100, -100]),
                    Body("obj2", 10**6, [100, 100])
    ) # simulation qui montre 2 terres à 20'000 kms l'une de l'autre
    c.start()

