import pygame

from pygame import Color
from board import initialise_board, draw_board
from event import events_setup
from screen import screen

pygame.init()

init = False

clock = pygame.time.Clock()

while True:
    dt = clock.tick(30) / 1000

    events_setup()

    screen.fill(Color(200, 250, 204))

    if not init:
        initialise_board()
        init = True

    draw_board()

    pygame.display.flip()

