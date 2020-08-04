#coding: utf-8
#!/usr/bin/env python3


import random
import time
import math
import sys
import pygame

from threading import Thread

# CONSTANTS
G = 6.67408e-11 * 1_000  # Otherwise the bodies would not move given the small value of gravitational constant
NUM_OF_BODIES = 100
WIDTH = 1000
HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (109, 196, 255)

class Body:
    def rcolor(self):
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def __init__(self, name, pos, a, v, m):
        self.name = name
        self.pos = pos  # pos is a list of x and y position of that body in pixels eg : [500,600]
        self.a = a  # a is a list of x and y components of accelaration of that body in pixel units
        self.v = v  # b is a list of x and y components of velocity of that body in pixel units
        self.m = m  # m is the mass of that object
        self.rcolor()

class Simulation(Thread):
    def do_play(self):
        self.play = True
        self.stop = False

    def do_pause(self):
        self.play = False
        self.stop = False

    def do_stop(self):
        self.play = False
        self.stop = True

    def __init__(self, bodies=None):
        super().__init__()

        if bodies == None:
            # bodies = [
            #     Body("A", [450, 450], [0, 0], [0, 0], 20),
            #     Body("B", [450, 550], [0, 0], [0, 0], 20),
            #     Body("C", [550, 450], [0, 0], [0, 0], 20),
            #     Body("D", [550, 550], [0, 0], [0, 0], 20),
            #     Body("O", [500, 500], [0, 0], [0, 0], 20)
            # ]
            bodies = [
                Body("A", [500, 500], [0, 0], [0, 0], 20),
                Body("B", [500, 500.001], [0, 0], [0, 0], 20)
            ]
        self.bodies = bodies

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

    def run(self):

        bodies = self.bodies

        pygame.init()
        size = WIDTH, HEIGHT
        screen = pygame.display.set_mode(size)

        font = pygame.font.SysFont('Arial', 16)
        text = font.render('0', True, BLUE)
        textRect = text.get_rect()

        self.do_play()
        while not self.stop:
            while self.play:
                in_t = time.time()
                screen.fill(BLACK)
                # events captures
                for event in pygame.event.get():
                    if event.type == pygame.K_ESCAPE:
                        self.do_stop()
                    if event.type == pygame.QUIT:
                        self.do_stop()

                # bodies' positions calcul and positionning on the window
                for body_a in bodies:
                    pos_a = body_a.pos
                    m_a = body_a.m
                    fx_total = 0
                    fy_total = 0

                    for body_b in bodies:
                        if body_b.pos == pos_a:
                            continue
                        fx, fy = self.calculate_forces(pos_a, body_b.pos, m_a, body_b.m)
                        fx_total += fx
                        fy_total += fy

                    body_a_acceleration = body_a.a

                    body_a_acceleration[0] = fx_total / m_a
                    body_a_acceleration[1] = fy_total / m_a

                    body_a.v[0] = body_a.v[0] + body_a_acceleration[0]
                    body_a.v[1] = body_a.v[1] + body_a_acceleration[1]

                    pos_a[0] = pos_a[0] + body_a.v[0]
                    pos_a[1] = pos_a[1] + body_a.v[1]

                    #mass_text = 'M={0}'.format(m_a)
                    #force_text = 'F=({0},{1})'.format(fx_total.__round__(3), fy_total.__round__(3))
                    #velocity_text = 'V=({},{})'.format(body_a.v[0].__round__(3),body_a.v[1].__round__(3))
                    #text_str = mass_text + '   ' + force_text + '   ' + velocity_text
                    text_str = body_a.name

                    text = font.render(text_str, True, BLUE)
                    textRect.center = (pos_a[0] + m_a + 10, pos_a[1] + m_a + 10)

                    screen.blit(text, textRect)
                    tmp_rect = pygame.Rect(pos_a[0], pos_a[1], m_a, m_a)
                    pygame.draw.circle(screen, body_a.color, tmp_rect.center, int(tmp_rect.width/2))

                pygame.display.flip()
                print(1/(time.time() - in_t))
        #sys.exit(0)


if __name__=="__main__":
    sim = Simulation()
    sim.start()
