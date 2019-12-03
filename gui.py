#coding: utf-8
#!/usr/bin/env python3

from random import randint as r

import pygame
from pygame.locals import *

def rcolor():
    return r(0, 255), r(0, 255), r(0, 255)

def gen(gravit):
    pass

def main(FPS=60, win_size=(640, 480)):
    pygame.init()

    spacetime = pygame.display.set_mode(win_size)

    fps_lim = pygame.time.Clock()
    pygame.key.set_repeat(400, 30)

    color = rcolor()
    obj1 = pygame.draw.circle(spacetime, color, (320, 240), 50)

    fond = pygame.Surface(win_size).convert()

    game_continue = True
    while game_continue:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_continue = False

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    obj1.move_ip(2, 0)
                if event.key == K_LEFT:
                    obj1.move_ip(-2, 0)
                if event.key == K_DOWN:
                    obj1.move_ip(0 ,2)
                if event.key == K_UP:
                    obj1.move_ip(0, -2)

        spacetime.blit(fond, (0, 0))

        obj1 = pygame.draw.circle(spacetime, color, obj1.center, 50)

        pygame.display.flip()
        fps_lim.tick(FPS)

main(60)
exit(0)
