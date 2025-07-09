import pygame

from pygame import Vector2
from screen import screen

white = (207, 250, 219)
d_white = (182, 219, 192)
green = (79, 168, 103)
d_green = (67, 143, 88)


class Tile:
    def __init__(self, center: Vector2, color: tuple):
        self.center = center
        self.color = color

        self.rect = pygame.Rect(self.center.x, self.center.y, 64, 64)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def darken(self):
        if self.color == green:
            self.color = d_green
        elif self.color == white:
            self.color = d_white

    def lighten(self):
        if self.color == d_green:
            self.color = green
        elif self.color == d_white:
            self.color = white

    def get_center(self):
        return self.center

    def get_rect(self):
        return self.rect
