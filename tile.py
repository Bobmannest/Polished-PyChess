import pygame
from pygame import Vector2
from piece import Piece
from screen import screen

class Tile:
    width = 64
    height = 64

    def __init__(self, center: Vector2, piece: Piece):
        self.center = center
        self.piece = piece

    #Getter
    def get_piece(self):
        return self.piece