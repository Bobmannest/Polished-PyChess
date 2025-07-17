import pygame

from screen import screen
from tile import board

square = pygame.image.load('misc_visuals/square.png')
square_resized = pygame.transform.scale(square, (64, 64))

turn = 'wt'

#temporary storage variables
currently_selected_piece = None
temp_selected_tile = None
temp_selected_piece = None

#Misc
def tile_hover_color_change(mouse_pos):
    for row in board:
        for tile in row:
            if tile.get_rect().collidepoint(mouse_pos):
                tile.darken_color()
            else:
                tile.normalise_color()


def board_reset_guarded():
    for row in board:
        for tile in row:
            if tile.get_piece() is not None:
                tile.get_piece().set_guarded(False)


#Mouse Click
def mouse_click_turn_check(tile_piece):
    global turn
    if turn in tile_piece.get_type():
        return True
    else:
        return False


def mouse_click_tile_check(mouse_pos, tile):
    if tile.get_rect().collidepoint(mouse_pos):
        if tile.get_piece() is not None:
            if mouse_click_turn_check(tile.get_piece()):
                global currently_selected_piece, temp_selected_piece, temp_selected_tile
                temp_selected_tile = tile
                temp_selected_piece = tile.get_piece()
                currently_selected_piece = tile.get_piece()
                tile.set_piece(None)
        else:
            currently_selected_piece = None


def mouse_click_board_check(mouse_pos):
    for row in board:
        for tile in row:
            mouse_click_tile_check(mouse_pos, tile)


#Mouse Drag
def piece_drag_available_move_visuals():
    for row in board:
        for tile in row:
            available_moves = (
                temp_selected_piece.get_available_moves(temp_selected_piece, temp_selected_tile.get_position(), board)
            )
            if tile.get_position() in available_moves:
                screen.blit(square_resized, (120 + tile.get_position()[1] * 64, 110 + tile.get_position()[0] * 64))


def piece_dragging_visuals(mouse_pos):
    if pygame.mouse.get_pressed()[0] and currently_selected_piece is not None:
        piece_drag_available_move_visuals()
        pygame.mouse.set_visible(0)
        piece_image = pygame.image.load('pieces/' + currently_selected_piece.get_type() + '.png')
        piece_image_resized = pygame.transform.scale(piece_image, (64, 64))
        screen.blit(piece_image_resized, (mouse_pos[0] - 32, mouse_pos[1] - 32))
    else:
        pygame.mouse.set_visible(1)


#Mouse Release
def turn_switch():
    global turn
    if 'wt' in turn:
        turn = 'bk'
    else:
        turn = 'wt'


def mouse_release_tile_check(mouse_pos, tile):
    global currently_selected_piece
    if tile.get_rect().collidepoint(mouse_pos):
        current_piece_available_moves = (
            temp_selected_piece.get_available_moves(temp_selected_piece, temp_selected_tile.get_position(), board)
        )
        if tile.get_position() in current_piece_available_moves:
            turn_switch()
            tile.set_piece(currently_selected_piece)
            currently_selected_piece = None
        else:
            temp_selected_tile.set_piece(temp_selected_piece)


def mouse_release_board_check(mouse_pos):
    for row in board:
        for tile in row:
            mouse_release_tile_check(mouse_pos, tile)


#Events setup
def mouse_events_setup(mouse_pos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board_reset_guarded()
            mouse_click_board_check(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP and currently_selected_piece is not None:
            mouse_release_board_check(mouse_pos)
    piece_dragging_visuals(mouse_pos)
