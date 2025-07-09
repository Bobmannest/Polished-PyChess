import pygame

from pygame import Color
from board import init_tiles, draw_tiles, draw_pieces
from event import mouse_events_setup, tile_hover_color_change
from screen import screen

pygame.init()

clock = pygame.time.Clock()

init_tiles()

while True:
    dt = clock.tick(30) / 1000 #delta time
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(Color(200, 250, 204))

    tile_hover_color_change(mouse_pos)
    draw_tiles()
    draw_pieces()
    mouse_events_setup(mouse_pos)


    pygame.display.flip()

