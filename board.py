import pygame

from screen import screen
from piece import Piece
from tile import Tile, white, green

black = (0, 0, 0)

center = pygame.Vector2(120, 110)
border_width = 8

#Initialise board
tile_board = [[None for _ in range(8)]for _ in range(8)]
piece_board = [[None for _ in range(8)] for _ in range(8)]

piece_board[0][0] = Piece('bk-rook')
piece_board[0][1] = Piece('bk-knight')
piece_board[0][2] = Piece('bk-bishop')
piece_board[0][3] = Piece('bk-queen')
piece_board[0][4] = Piece('bk-king')
piece_board[0][5] = Piece('bk-bishop')
piece_board[0][6] = Piece('bk-knight')
piece_board[0][7] = Piece('bk-rook')

piece_board[7][0] = Piece('wt-rook')
piece_board[7][1] = Piece('wt-knight')
piece_board[7][2] = Piece('wt-bishop')
piece_board[7][3] = Piece('wt-king')
piece_board[7][4] = Piece('wt-queen')
piece_board[7][5] = Piece('wt-bishop')
piece_board[7][6] = Piece('wt-knight')
piece_board[7][7] = Piece('wt-rook')

for tile in range(8):
    piece_board[1][tile] = Piece('bk-pawn')
    piece_board[6][tile] = Piece('wt-pawn')


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
    for row in range(8):
        for tile in range(8):
            #Display piece images
            tilex = center.x + tile * 64
            tiley = center.y + row * 64
            if piece_board[row][tile] is not None:
                image = pygame.image.load('pieces/' + piece_board[row][tile].get_type() + '.png')
                image_resized = pygame.transform.scale(image, (64, 64))
                screen.blit(image_resized, (tilex, tiley))




