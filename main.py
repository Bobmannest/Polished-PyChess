import pygame
from pygame import Color
from board import initialise_board
from event import events_setup
from screen import screen
from tile import Tile

pygame.init()

clock = pygame.time.Clock()

while True:
    dt = clock.tick(30) / 1000

    events_setup()

    screen.fill(Color(200, 250, 204))

    initialise_board()


    pygame.display.flip()

