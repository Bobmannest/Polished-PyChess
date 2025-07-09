import pygame

from board import tile_board
from piece import piece_board
from screen import screen


def tile_hover_color_change(mouse_pos):
    for row in tile_board:
        for tile in row:
            if tile.get_rect().collidepoint(mouse_pos):
                tile.darken()
            else:
                tile.lighten()


def mouse_events_setup(mouse_pos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mouse_is_held = pygame.mouse.get_pressed()
    if mouse_is_held[0]:
        for row in piece_board:
            for piece in row:
                if piece is not None:
                    if piece.get_rect().collidepoint(mouse_pos):
                        pygame.mouse.set_visible(0)
                        piece_image = pygame.image.load('pieces/' + piece.get_type() + '.png')
                        piece_image_resized = pygame.transform.scale(piece_image, (64, 64))
                        screen.blit(piece_image_resized, (mouse_pos[0] - 32, mouse_pos[1] - 32))
    else:
        pygame.mouse.set_visible(1)
