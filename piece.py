#Type: color-name
import pygame


class Piece:
    def __init__(self, type: str):
        self.type = type

    def calculate_available_moves(self, board):
        # Optional: raise NotImplementedError to force subclasses to implement this
        raise NotImplementedError('Use subclass versions!')

    def get_type(self):
        return self.type

class Pawn(Piece):
    def calculate_available_moves(self, board):
        print('pawn')

class Rook(Piece):
    def calculate_available_moves(self, board):
        print('rook')

class Knight(Piece):
    def calculate_available_moves(self, board):
        print('knight')

class Bishop(Piece):
    def calculate_available_moves(self, board):
        print('bishop')

class Queen(Piece):
    def calculate_available_moves(self, board):
        print('queen')

class King(Piece):
    def calculate_available_moves(self, board):
        print('king')