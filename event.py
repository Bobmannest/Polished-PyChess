import pygame

from screen import screen
from tile import board

selected_piece = None


def tile_hover_color_change(mouse_pos):
    for row in board:
        for tile in row:
            if tile.get_rect().collidepoint(mouse_pos):
                tile.darken()
            else:
                tile.lighten()


def mouse_events_setup(mouse_pos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for row in board:
                for tile in row:
                    if tile.get_piece() is not None:
                        if tile.get_rect().collidepoint(mouse_pos):
                            global selected_piece
                            selected_piece = tile.get_piece()
                    elif tile.get_piece() is None:
                        if tile.get_rect().collidepoint(mouse_pos):
                            selected_piece = None
        elif event.type == pygame.MOUSEBUTTONUP:
            print('up')

    if pygame.mouse.get_pressed()[0]:
        if selected_piece is not None:
            pygame.mouse.set_visible(0)
            piece_image = pygame.image.load('pieces/' + selected_piece.get_type() + '.png')
            piece_image_resized = pygame.transform.scale(piece_image, (64, 64))
            screen.blit(piece_image_resized, (mouse_pos[0] - 32, mouse_pos[1] - 32))
    else:
        pygame.mouse.set_visible(1)
