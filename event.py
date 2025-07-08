import pygame

from board import tile_board

def events_setup():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.set_visible(0)
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.mouse.set_visible(1)

def tile_hover_color_change():
    mouse_pos = pygame.mouse.get_pos()
    for row in tile_board:
        for tile in row:
            if tile.get_rect().collidepoint(mouse_pos):
                tile.darken()
            else:
                tile.lighten()