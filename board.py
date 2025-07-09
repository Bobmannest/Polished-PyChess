import pygame

from screen import screen
from piece import Piece, piece_board
from tile import Tile, white, green

black = (0, 0, 0)
center = pygame.Vector2(120, 110)
border_width = 8

#Initialise board
tile_board = [[None for _ in range(8)]for _ in range(8)]

Piece('bk-rook', [0, 0])
Piece('bk-knight', [0, 1])
Piece('bk-bishop', [0, 2])
Piece('bk-queen', [0, 3])
Piece('bk-king', [0, 4])
Piece('bk-bishop', [0, 5])
Piece('bk-knight', [0, 6])
Piece('bk-rook', [0, 7])

Piece('wt-rook', [7, 0])
Piece('wt-knight', [7, 1])
Piece('wt-bishop', [7, 2])
Piece('wt-king', [7, 3])
Piece('wt-queen', [7, 4])
Piece('wt-bishop', [7, 5])
Piece('wt-knight', [7, 6])
Piece('wt-rook', [7, 7])

for tile in range(8):
    Piece('bk-pawn', [1, tile])
    Piece('wt-pawn', [6, tile])


def color_pick(row, tile):
    if (row + tile) % 2 == 0:
        color = white
    else:
        color = green
    return color


def init_tiles():
    for row in range(8):
        for tile in range(8):
            color = color_pick(row, tile)
            tilex = center.x+tile*64
            tiley = center.y+row*64
            tile_board[row][tile] = Tile(pygame.Vector2(tilex, tiley), color)


def draw_tiles():
    pygame.draw.rect(screen, black, (center.x - border_width, center.y - border_width, 512 + 2 * border_width, 512 + 2 * border_width))
    for row in range(8):
        for tile in range(8):
            tile_board[row][tile].draw()
            


def draw_pieces():
    for row in piece_board:
        for piece in row:
            if piece is not None:
                piece.draw(screen)




