import pygame
import os


class Button:

    def __init__(self, position, images, size):
        self.images = {}
        for state in images:
            self.images[state] = pygame.transform.scale(pygame.image.load(images[state]), size)

        self.state = "unpressed"
        self.show = True

        self.position = position

    @property
    def image(self):
        return self.images[self.state]

    @property
    def rect(self):
        rect = self.image.get_rect()
        rect.x = self.position[0]
        rect.y = self.position[1]
        return rect

    def check_hold(self, pos):
        if self.rect.collidepoint(pos) and self.show:
            self.state = "pressed"

    def check_release(self):
        if self.state == "pressed":
            self.state = "unpressed"
            self.on_click()

    def update(self, screen):
        if self.show:
            screen.blit(self.image, self.rect)

    def on_click(self):
        pass

class HomeButton(Button):
    def __init__(self, position, camera_handler, size):
        super().__init__(position, {
            "pressed": "assets/buttons/home_pressed.png",
            "unpressed": "assets/buttons/home_unpressed.png"
        }, size)
        self.camera_handler = camera_handler

    def on_click(self):
        self.camera_handler.home()

class MainButton(Button):
    def __init__(self, position, children, size):
        print(os.getcwd())
        super().__init__(position, {
            "pressed": "assets/buttons/main_pressed.png",
            "unpressed": "assets/buttons/main_unpressed.png"
        }, size)
        self.active = False
        self.children = children

    def check_hold(self, pos):
        if self.rect.collidepoint(pos) and self.show:
            self.state = "pressed"
        for child in self.children:
            child.check_hold(pos)

    def check_release(self):
        if self.state == "pressed":
            self.state = "unpressed"
            self.on_click()
        for child in self.children:
            child.check_release()

    def update(self, screen):
        if self.show:
            screen.blit(self.image, self.rect)
        for child in self.children:
            child.update(screen)

    def on_click(self):
        self.active = not self.active
        for child in self.children:
            child.show = self.active

class PlayPauseButton(Button):
    def __init__(self, position, simulation, size):
        super().__init__(position, {
            "play_pressed":"assets/buttons/play_pressed.png",
            "play_unpressed":"assets/buttons/play_unpressed.png",
            "pause_pressed":"assets/buttons/pause_pressed.png",
            "pause_unpressed":"assets/buttons/pause_unpressed.png"
        }, size)

        self.simulation = simulation


    @property
    def image(self):
        if self.simulation.play:
            if self.state == "pressed":
                return self.images["play_pressed"]
            if self.state == "unpressed":
                return self.images["play_unpressed"]
        else:
            if self.state == "pressed":
                return self.images["pause_pressed"]
            if self.state == "unpressed":
                return self.images["pause_unpressed"]

    def on_click(self):
        self.simulation.play = not self.simulation.play

class ZoomInButton(Button):
    def __init__(self, position, camera_handler, size):
        super().__init__(position, {
            "pressed": "assets/buttons/zoom_in_pressed.png",
            "unpressed": "assets/buttons/zoom_in_unpressed.png"
        }, size)

        self.camera_handler = camera_handler

    def on_click(self):
        self.camera_handler.zoom_in(1.1)


class ZoomOutButton(Button):
    def __init__(self, position, camera_handler, size):
        super().__init__(position, {
            "pressed": "assets/buttons/zoom_in_pressed.png",
            "unpressed": "assets/buttons/zoom_in_unpressed.png"
        }, size)

        self.camera_handler = camera_handler

    def on_click(self):
        self.camera_handler.zoom_out(1.1)
