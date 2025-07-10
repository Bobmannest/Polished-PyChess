import pygame

from screen import screen
from piece import Piece
from tile import Tile, board, white, green

black = (0, 0, 0)
center = pygame.Vector2(120, 110)
border_width = 8


def color_pick(row, tile):
    if (row + tile) % 2 == 0:
        color = white
    else:
        color = green
    return color


def init_tiles():
    for row in range(8):
        for tile in range(8):
            board[row][tile] = Tile([row, tile], color_pick(row, tile), None)

def init_pieces():
    board[0][0].set_piece(Piece('bk-rook'))
    board[0][1].set_piece(Piece('bk-knight'))
    board[0][2].set_piece(Piece('bk-bishop'))
    board[0][3].set_piece(Piece('bk-queen'))
    board[0][4].set_piece(Piece('bk-king'))
    board[0][5].set_piece(Piece('bk-bishop'))
    board[0][6].set_piece(Piece('bk-knight'))
    board[0][7].set_piece(Piece('bk-rook'))

    board[7][0].set_piece(Piece('wt-rook'))
    board[7][1].set_piece(Piece('wt-knight'))
    board[7][2].set_piece(Piece('wt-bishop'))
    board[7][3].set_piece(Piece('wt-queen'))
    board[7][4].set_piece(Piece('wt-king'))
    board[7][5].set_piece(Piece('wt-bishop'))
    board[7][6].set_piece(Piece('wt-knight'))
    board[7][7].set_piece(Piece('wt-rook'))

    for tile in range(8):
        board[1][tile].set_piece(Piece('bk-pawn'))
        board[6][tile].set_piece(Piece('wt-pawn'))


def draw_board():
    pygame.draw.rect(screen, black, (center.x - border_width, center.y - border_width, 512 + 2 * border_width, 512 + 2 * border_width))
    for row in board:
        for tile in row:
            board[tile.get_position()[1]][tile.get_position()[0]].draw()






