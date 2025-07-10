import pygame

from pygame import Color
from board import init_tiles, draw_board, init_pieces
from event import mouse_events_setup, tile_hover_color_change
from tile import board_check
from screen import screen

pygame.init()

clock = pygame.time.Clock()

init_tiles()
init_pieces()
init = True

while True:
    dt = clock.tick(60) / 1000 #delta time and clock tick for FPS
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(Color(200, 250, 204))

    tile_hover_color_change(mouse_pos)
    draw_board()
    mouse_events_setup(mouse_pos)
    if init:
        board_check()
        init = False


    pygame.display.flip()

