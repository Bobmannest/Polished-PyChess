import pygame

from screen import screen
from piece import Piece

black = (0, 0, 0)
white = (207, 250, 219)
green = (79, 168, 103)

center = pygame.Vector2(120, 110)
border_width = 8

board = [[None for _ in range(8)]for _ in range(8)]
board[0][0] = Piece('white', 'rook')

def color_pick(row, tile):
    if (row + tile) % 2 == 0:
        color = white
    else:
        color = green
    return color

def draw_board():
    pygame.draw.rect(screen, black, (center.x - border_width, center.y - border_width, 512 + 2 * border_width, 512 + 2 * border_width))
    for row in range(8):
        for tile in range(8):
            color = color_pick(row, tile)
            tilex = center.x+row*64
            tiley = center.y+tile*64
            pygame.draw.rect(screen, color, (tilex, tiley, 64, 64))

            if board[row][tile] is None:
                pass
            else:
                print(row, tile)
                image = pygame.image.load('pieces/'+board[row][tile].get_side()+'-'+board[row][tile].get_type()+'.png')
                image_resized = pygame.transform.scale(image, (64, 64))
                screen.blit(image_resized, (tilex, tiley))




