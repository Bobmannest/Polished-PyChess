import pygame

from pygame import Color
from board_init import init_tiles, init_pieces, test_init_pieces
from event import mouse_events_setup, tile_hover_color_change
from tile import draw_board
from screen import screen

pygame.init()

clock = pygame.time.Clock()

init_tiles()
#test_init_pieces()
init_pieces()

while True:
    dt = clock.tick(60) / 1000 #delta time and clock tick for FPS
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(Color(200, 250, 204))

    tile_hover_color_change(mouse_pos)
    draw_board()
    mouse_events_setup(mouse_pos)

    pygame.display.flip()

