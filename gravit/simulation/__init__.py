# coding: utf-8
# !/usr/bin/env python3

import pygame
from threading import Thread

from . import physic

# CONSTANTS
WIDTH = 1000
HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (109, 196, 255)


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

        if bodies is None:
            bodies = [
                physic.Body("A", [450, 450], [0, 0], [0, 1], 20),
                physic.Body("B", [450, 550], [0, 0], [1, 0], 20),
                physic.Body("C", [550, 450], [0, 0], [0, -1], 20),
                physic.Body("D", [550, 550], [0, 0], [-1, 0], 20),
                physic.Body("O", [500, 500], [0, 0], [0, 0], 20)
            ]
            # bodies = [
            #     physic.Body("A", [500, 500], [0, 0], [0, 0], 20),
            #     physic.Body("B", [500, 500.001], [0, 0], [0, 0], 20)
            # ]
        self.bodies = bodies

    def display_body(self, body, label=''):
        self.body_label = self.labelFont.render(label, True, BLUE)
        self.body_labelRect.center = (body.pos[0] + body.m + 10, body.pos[1] + body.m + 10)

        self.screen.blit(self.body_label, self.body_labelRect)
        tmp_rect = pygame.Rect(body.pos[0], body.pos[1], body.m, body.m)
        pygame.draw.circle(self.screen, body.color, tmp_rect.center, int(tmp_rect.width / 2))

    def run(self):

        bodies = self.bodies

        pygame.init()
        size = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(size)

        self.labelFont = pygame.font.SysFont('Arial', 16)
        self.body_label = self.labelFont.render('', True, BLUE)
        self.body_labelRect = self.body_label.get_rect()

        fps_clock = pygame.time.Clock()

        self.do_play()
        while not self.stop:
            while self.play:
                self.screen.fill(BLACK)
                # events captures
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.do_stop()
                        exit(0)

                    if event.type == pygame.KEYDOWN:
                        # check for debug screen key
                        if event.key == pygame.K_F3:  # yes the debug screen key is from Minecraft :)
                            try:
                                display_debug_screen = not display_debug_screen
                            except UnboundLocalError:
                                display_debug_screen = True
                        # check for pause key
                        if event.key == pygame.K_SPACE:
                            self.do_pause()
                        # check for exit/stop key
                        if event.key == pygame.K_ESCAPE:
                            self.do_stop()
                            return

                for body_a in bodies:
                    pos_a = body_a.pos
                    m_a = body_a.m
                    fx_total = 0
                    fy_total = 0

                    for body_b in bodies:
                        if body_b.pos == pos_a:
                            continue
                        fx, fy = physic.calculate_forces(pos_a, body_b.pos, m_a, body_b.m)
                        fx_total += fx
                        fy_total += fy

                    body_a_acceleration = body_a.a

                    body_a_acceleration[0] = fx_total / m_a
                    body_a_acceleration[1] = fy_total / m_a

                    body_a.v[0] = body_a.v[0] + body_a_acceleration[0]
                    body_a.v[1] = body_a.v[1] + body_a_acceleration[1]

                    pos_a[0] = pos_a[0] + body_a.v[0]
                    pos_a[1] = pos_a[1] + body_a.v[1]

                    # LABEL DEFINITION
                    # mass_text = 'M={0}'.format(m_a)
                    # force_text = 'F=({0},{1})'.format(fx_total.__round__(3), fy_total.__round__(3))
                    # velocity_text = 'V=({},{})'.format(body_a.v[0].__round__(3),body_a.v[1].__round__(3))
                    # text_str = mass_text + '   ' + force_text + '   ' + velocity_text
                    label_text = body_a.name

                    self.display_body(body_a, label_text)

                try:
                    if display_debug_screen:
                        debug_screen_text = "FPS: " + str(round(fps_clock.get_fps()))
                        debug_screen_label = self.labelFont.render(debug_screen_text, True, BLUE)
                        debug_screen_labelRect = debug_screen_label.get_rect()
                        debug_screen_labelRect.x = 5
                        debug_screen_labelRect.y = 5
                        self.screen.blit(debug_screen_label, debug_screen_labelRect)
                except UnboundLocalError:
                    pass

                pygame.display.flip()
                fps_clock.tick()

            self.screen.fill(BLACK)
            # events captures
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.do_stop()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    # check for debug screen key
                    if event.key == pygame.K_F3:  # yes the debug screen key is from Minecraft :)
                        try:
                            display_debug_screen = not display_debug_screen
                        except UnboundLocalError:
                            display_debug_screen = True
                    # check for play key
                    if event.key == pygame.K_SPACE:
                        self.do_play()
                    # check for exit/stop key
                    if event.key == pygame.K_ESCAPE:
                        self.do_stop()
                        exit(0)

            for body_a in bodies:

                # no body movement

                # LABEL DEFINITION
                # mass_text = 'M={0}'.format(m_a)
                # force_text = 'F=({0},{1})'.format(fx_total.__round__(3), fy_total.__round__(3))
                # velocity_text = 'V=({},{})'.format(body_a.v[0].__round__(3),body_a.v[1].__round__(3))
                # text_str = mass_text + '   ' + force_text + '   ' + velocity_text
                label_text = body_a.name

                self.display_body(body_a, label_text)

            try:
                if display_debug_screen:
                    debug_screen_text = "FPS: " + str(round(fps_clock.get_fps()))
                    debug_screen_label = self.labelFont.render(debug_screen_text, True, BLUE)
                    debug_screen_labelRect = debug_screen_label.get_rect()
                    debug_screen_labelRect.x = 5
                    debug_screen_labelRect.y = 5
                    self.screen.blit(debug_screen_label, debug_screen_labelRect)
            except UnboundLocalError:
                pass

            pygame.display.flip()
            fps_clock.tick()

        # sys.exit(0)
