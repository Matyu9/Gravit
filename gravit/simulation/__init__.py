#coding: utf-8
#!/usr/bin/env python3

import pygame
from pygame.locals import *

from random import randint as r
from threading import Thread

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

    def rcolor(self):
        color = r(0, 255), r(0, 255), r(0, 255)
        return color

    def __init__(self, FPS=60, win_size=(640, 480)):
        super().__init__()

        self.FPS = FPS
        self.win_size = win_size

    def run(self):

        pygame.init()

        pygame.display.set_caption("Gravit Simulation")
        self.spacetime = pygame.display.set_mode(self.win_size)

        self.fps_clock = pygame.time.Clock()
        pygame.key.set_repeat(400, 30)

        #affichage du bg
        self.bg = pygame.Surface(self.win_size).convert()
        #blit du bg
        self.spacetime.blit(self.bg, (0, 0))

        #setup de l'astre
        self.obj1 = pygame.Surface((100, 100))
        pygame.draw.circle(self.obj1, self.rcolor(), (50, 50), 50)
        # 1er affichage
        self.spacetime.blit(self.obj1, (320, 240))
        self.obj1_rect = self.obj1.get_rect()

        self.do_play()
        #boucle de jeu
        while not self.stop:
            while self.play:
                #events et leurs reactions
                for event in pygame.event.get():

                    if event.type == QUIT:
                        self.do_stop()
                        pygame.quit()
                        exit(0)

                    if event.type == KEYDOWN:

                        if event.key == K_RIGHT:
                            self.obj1_rect.move_ip(2, 0)
                            self.obj1_rect.move_ip(2, 0)

                        if event.key == K_LEFT:
                            self.obj1_rect.move_ip(-2, 0)
                            self.obj1_rect.move_ip(-2, 0)


                        if event.key == K_DOWN:
                            self.obj1_rect.move_ip(0 ,2)
                            self.obj1_rect.move_ip(0 ,2)

                        if event.key == K_UP:
                            self.obj1_rect.move_ip(0, -2)
                            self.obj1_rect.move_ip(0, -2)


                self.spacetime.blit(self.bg, (0, 0))

                self.spacetime.blit(self.obj1, self.obj1_rect)

                pygame.display.flip()

                self.fps_clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.do_stop()
                    pygame.quit()
                    exit(0)

            self.spacetime.blit(self.bg, (0, 0))

            self.spacetime.blit(self.obj1, self.obj1_rect)

            pygame.display.flip()

            self.fps_clock.tick(self.FPS)


if __name__=="__main__":
    sim = Simulation()
    sim.start()
