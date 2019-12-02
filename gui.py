#coding: utf-8
#!/usr/bin/env python3

from random import randint as r

import pygame
from pygame.locals import *

def rcolor():
    return r(0, 255), r(0, 255), r(0, 255)

def gen(gravit):
    pass

def main(FPS):
    pygame.init()

    spacetime = pygame.display.set_mode((640, 480))

    fps_lim = pygame.time.Clock()

    obj1 = pygame.draw.circle(spacetime, rcolor(), (320, 240), 50)

    game_continue = True
    while game_continue:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_continue = False

        obj1.move_ip(3, 3)

        pygame.display.update()
        fps_lim.tick(FPS)

main(30)
exit(0)
