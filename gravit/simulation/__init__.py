# coding: utf-8

import pygame
from threading import Thread

from . import physic

# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (109, 196, 255)

CAM_DEPLACEMENT = 5


class CameraHandler:
    def __init__(self, resolution, zoom=1.0, camera_pos=(0, 0)):
        self.resolution = resolution
        self.zoom = zoom
        self.camera_pos = camera_pos

    def move_camera(self, x, y):
        self.camera_pos = (
            self.camera_pos[0]+x,
            self.camera_pos[1]+y,
        )

    def zoom_in(self, delta):
        self.zoom *= delta

    def zoom_out(self, delta):
        self.zoom /= delta

    def convert_pos(self, pos):
        return [
            pos[0] * self.zoom + self.resolution[0]/2 - self.camera_pos[0],
            pos[1] * self.zoom + self.resolution[1]/2 - self.camera_pos[1]
        ]
        # was
        # return [
        #             pos[0] * self.zoom + self.resolution[0] - self.camera_pos[0],
        #             pos[1] * self.zoom + self.resolution[1] - self.camera_pos[1]
        #         ]

    def convert_radius(self, radius):
        return radius * self.zoom


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
        pygame.quit()

    def __init__(self, bodies=None, resolution=(1280, 720)):
        super().__init__()

        if bodies is None:
            bodies = [
                physic.Body("A", [-100, -100], [0, 0], [0, 0], 50),
                physic.Body("B", [200, 200], [0, 0], [0, 0], 50),
                physic.Body("O", [0, 0], [0, 0], [0, 0], 50)
            ]
            # bodies = [
            #     physic.Body("A", [0, 0], [0, 0], [0, 0], 50)
            # ]

        self.bodies = bodies

        self.resolution = resolution

    def display_body(self, body, label=''):
        self.body_label = self.labelFont.render(label, True, BLUE)
        body_diameter = self.camera_handler.convert_radius(body.radius) * 2
        body_pos = self.camera_handler.convert_pos(body.pos)

        self.body_labelRect.center = (body_pos[0] + body_diameter / 2 + 10, body_pos[1] + body_diameter / 2 + 10)

        self.screen.blit(self.body_label, self.body_labelRect)
        tmp_rect = pygame.Rect(body_pos[0], body_pos[1], body_diameter, body_diameter)
        pygame.draw.circle(self.screen, body.color, (tmp_rect.x, tmp_rect.y), int(tmp_rect.width / 2))

    def run(self):

        bodies = self.bodies

        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)

        self.labelFont = pygame.font.SysFont('Arial', 16)
        self.body_label = self.labelFont.render('', True, BLUE)
        self.body_labelRect = self.body_label.get_rect()

        self.camera_handler = CameraHandler(self.resolution)
        move_camera = False
        display_debug_screen = False


        fps_clock = pygame.time.Clock()

        self.do_play()
        while not self.stop:
            self.screen.fill(BLACK)
            # events captures
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.do_stop()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    # check for debug screen key
                    if event.key == pygame.K_F3:  # yes, the debug screen key is from Minecraft :)
                        display_debug_screen = True
                    # check for pause key
                    if event.key == pygame.K_SPACE:
                        if self.play:
                            self.do_pause()
                        else:
                            self.do_play()

                    if event.key == pygame.K_UP:
                        self.camera_handler.move_camera(0, -CAM_DEPLACEMENT)
                    if event.key == pygame.K_DOWN:
                        self.camera_handler.move_camera(0, CAM_DEPLACEMENT)
                    if event.key == pygame.K_LEFT:
                        self.camera_handler.move_camera(-CAM_DEPLACEMENT, 0)
                    if event.key == pygame.K_RIGHT:
                        self.camera_handler.move_camera(CAM_DEPLACEMENT, 0)

                    # check for exit/stop key
                    if event.key == pygame.K_ESCAPE:
                        self.do_stop()
                        return

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F3:
                        display_debug_screen = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        move_camera = True
                    if event.button == 4:
                        self.camera_handler.zoom_in(1.1)
                    if event.button == 5:
                        self.camera_handler.zoom_out(1.1)

                if event.type == pygame.MOUSEBUTTONUP:
                    move_camera = False

                if event.type == pygame.MOUSEMOTION:
                    if move_camera:
                        self.camera_handler.move_camera(-event.rel[0], -event.rel[1])

            if self.play:
                for key_a, body_a in enumerate(bodies):
                    pos_a = body_a.pos
                    m_a = body_a.m
                    fx_total = 0
                    fy_total = 0

                    for key_b, body_b in enumerate(bodies):
                        if body_b.pos == pos_a:
                            continue
                        if physic.check_collision(body_a, body_b):
                            bodies[key_a] = physic.merge_bodies(body_a, body_b)
                            del bodies[key_b]
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
            else:
                for body_a in bodies:

                    # no body movement

                    # LABEL DEFINITION
                    # mass_text = 'M={0}'.format(m_a)
                    # force_text = 'F=({0},{1})'.format(fx_total.__round__(3), fy_total.__round__(3))
                    # velocity_text = 'V=({},{})'.format(body_a.v[0].__round__(3),body_a.v[1].__round__(3))
                    # text_str = mass_text + '   ' + force_text + '   ' + velocity_text
                    label_text = body_a.name

                    self.display_body(body_a, label_text)

            if display_debug_screen:
                debug_screen_text = "FPS: " + str(round(fps_clock.get_fps()))
                debug_screen_label = self.labelFont.render(debug_screen_text, True, BLUE)
                debug_screen_labelRect = debug_screen_label.get_rect()
                debug_screen_labelRect.x = 5
                debug_screen_labelRect.y = 5
                self.screen.blit(debug_screen_label, debug_screen_labelRect)

            pygame.display.flip()
            fps_clock.tick()

        # exit(0)
