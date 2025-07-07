import pygame

from screen import screen
from tile import Tile

black = (0, 0, 0)
white = (207, 250, 219)
green = (79, 168, 103)

center = pygame.Vector2(120, 110)
border_width = 8

board = [
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
]

def color_pick(row, tile):
    if (row + tile) % 2 == 0:
        color = white
    else:
        color = green
    return color

def initialise_board():
    pygame.draw.rect(screen, black, (center.x-border_width, center.y-border_width, 512+2*border_width, 512+2*border_width))
    for row in range(8):
        for tile in range(8):
            board[row][tile] = Tile(pygame.Vector2(center.x + (64 * row), center.y + (64 * tile)), None)

def draw_board():
    pygame.draw.rect(screen, black, (center.x - border_width, center.y - border_width, 512 + 2 * border_width, 512 + 2 * border_width))
    for row in range(8):
        for tile in range(8):
            color = color_pick(row, tile)
            tilex = center.x+row*64
            tiley = center.y+tile*64
            pygame.draw.rect(screen, color, (tilex, tiley, Tile.width, Tile.height))

            if board[row][tile].get_piece() is None:
                pass
            else:
                image = board[row][tile].get_piece().get_type() + '.jpg'
                screen.blit(image, (tilex, tiley))




