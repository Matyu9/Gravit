import random
import math

# CONSTANTS
G = 6.67408e-11 * 1_000_000_000  # Otherwise the bodies would not move given the small value of gravitational constant


class Body:

    def __init__(self, name, pos, a, v, m, color=None, radius=None):
        self.name = name
        self.pos = pos  # pos is a list of x and y position of that body in pixels eg : [500,600]
        self.a = a  # a is a list of x and y components of acceleration of that body in pixel units
        self.v = v  # b is a list of x and y components of velocity of that body in pixel units
        self.m = m  # m is the mass of that object
        if color is None:
            self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        else:
            self.color = color
        if radius is None:
            self.radius = self.m
        else:
            self.radius = radius


def calculate_forces(pos_a, pos_b, m_a, m_b):
    x_diff = pos_b[0] - pos_a[0]
    y_diff = pos_b[1] - pos_a[1]
    hypotenuse = math.sqrt((x_diff ** 2 + y_diff ** 2))
    sin = x_diff / hypotenuse
    cos = y_diff / hypotenuse
    f = G * m_a * m_b / hypotenuse ** 2
    fx = f * sin
    fy = f * cos

    return fx, fy


def check_collision(a, b):
    distance = math.sqrt(
        (a.pos[0] - b.pos[0]) ** 2
        + (a.pos[1] - b.pos[1]) ** 2
    )
    return distance <= (a.radius + b.radius)


def merge_bodies(a, b):
    name = a.name + " + " + b.name
    mass = a.m + b.m
    pos = [
        a.pos[0] * a.m / mass + b.pos[0] * b.m / mass,
        a.pos[1] * a.m / mass + b.pos[1] * b.m / mass
    ]
    velocity = [
        a.v[0] * a.m / mass + b.v[0] * b.m / mass,
        a.v[1] * a.m / mass + b.v[1] * b.m / mass
    ]
    acceleration = [
        a.a[0] * a.m / mass + b.a[0] * b.m / mass,
        a.a[1] * a.m / mass + b.a[1] * b.m / mass
    ]
    color = (
        (a.color[0] + b.color[0]) / 2,
        (a.color[1] + b.color[1]) / 2,
        (a.color[2] + b.color[2]) / 2
    )
    radius = (a.m / a.radius + b.m / b.radius) / 2
    return Body(name, pos, acceleration, velocity, mass, color, radius)
