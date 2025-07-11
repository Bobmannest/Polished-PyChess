import pygame
from typing import Optional
from pygame import Vector2

from piece import Piece
from screen import screen

center = pygame.Vector2(120, 110)
border_width = 8

black = (0, 0, 0)
white = (207, 250, 219)
d_white = (182, 219, 192)
green = (79, 168, 103)
d_green = (67, 143, 88)

board = [[None for _ in range(8)] for _ in range(8)]

class Tile:
    def __init__(self, position: list, color: tuple, piece: Optional[Piece] = None):
        self.position = position
        self.color = color
        self.piece = piece

        self.rect = pygame.Rect(120+self.position[1]*64, 110+self.position[0]*64, 64, 64)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.piece is not None:
            piece_image = pygame.image.load('pieces/' + self.piece.get_type() + '.png')
            piece_image_resized = pygame.transform.scale(piece_image, (64, 64))
            screen.blit(piece_image_resized, (120 + self.position[1] * 64, 110 + self.position[0] * 64))

    def darken(self):
        if self.color == green:
            self.color = d_green
        elif self.color == white:
            self.color = d_white

    def lighten(self):
        if self.color == d_green:
            self.color = green
        elif self.color == d_white:
            self.color = white

    def get_position(self):
        return self.position

    def get_rect(self):
        return self.rect

    def get_piece(self):
        return self.piece

    def set_piece(self, new_piece:Optional[Piece] = None):
        self.piece = new_piece


def draw_board():
    pygame.draw.rect(screen, black, (center.x - border_width, center.y - border_width, 512 + 2 * border_width, 512 + 2 * border_width))
    for row in board:
        for tile in row:
            board[tile.get_position()[1]][tile.get_position()[0]].draw()


def board_check():
    for row in board:
        row_types = ''
        for tile in row:
            if tile.get_piece() is not None:
                piece_type = tile.get_piece().get_type()
            else:
                piece_type = 'none'
            row_types += piece_type
            row_types += ' '
        print(row_types)
    print('\n')