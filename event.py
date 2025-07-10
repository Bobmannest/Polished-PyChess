import pygame

from screen import screen
from tile import board, board_check

#temporary storage variables
currently_selected_piece = None
temp_tile = None
temp_piece = None


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
            #Make into function rn
            for row in board:
                for tile in row:
                    if tile.get_rect().collidepoint(mouse_pos):
                        if tile.get_piece() is not None:
                            global currently_selected_piece, temp_piece, temp_tile
                            temp_tile = tile
                            temp_piece = tile.get_piece()
                            currently_selected_piece = tile.get_piece()
                            tile.set_piece(None)
                        else:
                            currently_selected_piece = None

        elif event.type == pygame.MOUSEBUTTONUP and currently_selected_piece is not None:
            # Make into function rn
            for row in board:
                for tile in row:
                    if tile.get_rect().collidepoint(mouse_pos):
                        if tile.get_piece() is None:
                            tile.set_piece(currently_selected_piece)
                        else:
                            temp_tile.set_piece(temp_piece)
                            print('fail')
            board_check()

    if pygame.mouse.get_pressed()[0]:
        if currently_selected_piece is not None:
            pygame.mouse.set_visible(0)
            piece_image = pygame.image.load('pieces/' + currently_selected_piece.get_type() + '.png')
            piece_image_resized = pygame.transform.scale(piece_image, (64, 64))
            screen.blit(piece_image_resized, (mouse_pos[0] - 32, mouse_pos[1] - 32))
    else:
        pygame.mouse.set_visible(1)
