import pygame

from pygame import Color
from board import init_tiles, draw_tiles, draw_pieces
from event import events_setup, tile_hover_color_change
from screen import screen

pygame.init()

clock = pygame.time.Clock()

init_tiles()

while True:
    dt = clock.tick(30) / 1000 #delta time

    screen.fill(Color(200, 250, 204))

    events_setup()
    tile_hover_color_change()
    draw_tiles()
    draw_pieces()

    pygame.display.flip()

