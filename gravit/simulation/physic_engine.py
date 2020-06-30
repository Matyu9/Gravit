import math
import time
from threading import Thread


class ValueInTime:
    """ValueInTime is no longer used as cache system. It's only here for compatibility. (yes I'm lazy :P)"""
    def __init__(self, value):
        self.value = value
    def get(self, time):
        return self.value

    def set(self, time, value):
        self.value = value


class Body:
    def __init__(self, name, mass, pos, acceleration=[0, 0], velocity=[0, 0]):
        self.name = name
        self.m = mass  # mass is the mass of that object
        self.pos = ValueInTime(pos)  # pos is a list of x and y position of that body in pixels eg : [500,600]
        self.a = ValueInTime(acceleration)  # acceleration is a list of x and y components of accelaration of that body in pixel units
        self.v = ValueInTime(velocity)  # velocity is a list of x and y components of velocity of that body in pixel units


## Constantes de la Physique
G = 1


class GravityEngine(Thread):

    def do_play(self):
        self.play = True
        self.stop = False

    def do_pause(self):
        self.play = False
        self.stop = False

    def do_stop(self):
        self.play = False
        self.stop = True

    def __init__(self, bodies, TPS=15, delta=None):
        super().__init__()
        self.bodies = bodies
        self.time = 0.0
        self.max_tps = TPS
        if delta == None:
            self.delta = 1 / self.max_tps
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
            pos_a = body_a.pos.get(self.time)
            m_a = body_a.m
            fx_total = 0
            fy_total = 0

            for body_b in self.bodies:
                if body_b.pos.get(self.time) == pos_a:
                    continue
                # on calcule les forces applique sur les astres
                fx, fy = self.calculate_forces(pos_a, body_b.pos.get(self.time), m_a, body_b.m)
                fx_total += fx
                fy_total += fy

            body_a_acceleration = body_a.a.get(self.time)

            # apres avoir calcule les forces, on calcule l'acceleration
            body_a_acceleration[0] = fx_total / m_a
            body_a_acceleration[1] = fy_total / m_a

            # on applique l'acceleration a l'obj Body
            body_a.a.set(self.time, body_a_acceleration)

            body_a_velocity = body_a.a.get(self.time)

            # on calcule la velocite
            body_a_velocity[0] += body_a_acceleration[0] * self.delta
            body_a_velocity[1] += body_a_acceleration[1] * self.delta

            # on l'applique a Body
            body_a.v.set(self.time, body_a_velocity)

            # pas de pos_a = [...].get(self.time) car fait plus haut (ligne 87)

            # on calcule la postion
            pos_a[0] += 0.5 * body_a_acceleration[0] * self.delta * self.delta + body_a.v.get(self.time)[0] * self.delta
            pos_a[1] += 0.5 * body_a_acceleration[1] * self.delta * self.delta + body_a.v.get(self.time)[1] * self.delta

            # on l'applique a Body
            body_a.pos.set(self.time, pos_a)

            # Infos de debug
            if __name__ == "__main__":
                print("[{}] : {} ".format(body_a.name, body_a.pos.value))

        self.run_speed = time.time() - in_t
        self.time += round(self.delta, 6)
        # infos de debug
        if __name__ == "__main__":
            print("t =", self.time)

    def run(self):
        t = 0.0
        self.do_play()
        while not self.stop:
            while self.play:
                self.apply_forces()
                self.TPS = 1 / (self.max_tps) - self.run_speed
                time.sleep(1 / self.max_tps)


if __name__ == "__main__":
    c = GravityEngine(
        [Body("obj1", 10 ** 6, [-100, -100]),
         Body("obj2", 10 ** 6, [100, 100])]
    )
    c.start()
