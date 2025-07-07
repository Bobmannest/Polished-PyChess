import pygame
from pygame import Vector2
from piece import Piece
from screen import screen

class Tile:
    width = 64
    height = 64

    #def __init__(self, center: Vector2, color: tuple, piece: Piece):
        #self.piece = piece
    def __init__(self, center: Vector2, color: tuple, piece: Piece):
        self.center = center
        self.color = color
        self.Piece = Piece

        pygame.draw.rect(screen, color, (center.x, center.y, Tile.width, Tile.height))

