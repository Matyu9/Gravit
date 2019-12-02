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
    color = rcolor()
    obj1 = pygame.draw.circle(spacetime, color, (320, 240), 50)

    game_continue = True
    while game_continue:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_continue = False

        obj1.move_ip(3, 0)
        # mettre un fond
        fond = pygame.image.load("background.jpg").convert()

        obj1 = pygame.draw.circle(spacetime, color, (obj1.x+50, obj1.y+50), 50)

        pygame.display.update()
        fps_lim.tick(FPS)

main(10)
exit(0)
