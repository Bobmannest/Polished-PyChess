#Type: color-name
import pygame

class Piece:
    def __init__(self, type: str):
        self.type = type

    def get_type(self):
        return self.type
