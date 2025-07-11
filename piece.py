import pygame

class Piece:
    def __init__(self, type: str):
        self.type = type

    def get_available_moves(self, tile_pos, board):
        # Optional: raise NotImplementedError to force subclasses to implement this
        raise NotImplementedError('Use subclass versions!')

    def get_type(self):
        return self.type

class Pawn(Piece):
    def get_available_moves(self, tile_pos, board):
        print('pawn')

class Rook(Piece):
    def get_available_moves(self, tile_pos, board):
        available_moves = []
        row, tile = tile_pos

        t = tile - 1
        while t >= 0:
            available_moves.append([row, t])
            t -= 1
        t = tile + 1
        while t <= 7:
            available_moves.append([row, t])
            t += 1
        r = row - 1
        while r >= 0:
            available_moves.append([r, t])
            r -= 1
        r = row + 1
        while r <= 7:
            available_moves.append([r, t])
            r += 1
        return available_moves

class Knight(Piece):
    def get_available_moves(self, tile_pos, board):
        print('knight')

class Bishop(Piece):
    def get_available_moves(self, tile_pos, board):
        print('bishop')

class Queen(Piece):
    def get_available_moves(self, tile_pos, board):
        print('queen')

class King(Piece):
    def get_available_moves(self, tile_pos, board):
        print('king')