import pygame

from pygame import Color
from board import draw_board
from event import events_setup
from screen import screen

pygame.init()

clock = pygame.time.Clock()

while True:
    dt = clock.tick(30) / 1000

    events_setup()

    screen.fill(Color(200, 250, 204))

    draw_board()

    pygame.display.flip()

