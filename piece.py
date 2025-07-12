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
        available_moves = []
        row, tile = tile_pos
        if 'wt' in self.type:
            available_moves.append([row - 1, tile])
        elif 'bk' in self.type:
            available_moves.append([row + 1, tile])
        return tile_occupied_check(board, available_moves)


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
        t = tile
        while r >= 0:
            available_moves.append([r, t])
            r -= 1
        r = row + 1
        while r <= 7:
            available_moves.append([r, t])
            r += 1
        return tile_occupied_check(board, available_moves)


class Knight(Piece):
    def get_available_moves(self, tile_pos, board):
        available_moves = []
        row, tile = tile_pos

        t = tile + 2
        available_moves.append([row + 1, t]), available_moves.append([row - 1, t])
        t = tile - 2
        available_moves.append([row + 1, t]), available_moves.append([row - 1, t])
        t = tile - 1
        available_moves.append([row + 2, t]), available_moves.append([row - 2, t])
        t = tile + 1
        available_moves.append([row + 2, t]), available_moves.append([row - 2, t])

        return tile_occupied_check(board, available_moves)
class Bishop(Piece):
    def get_available_moves(self, tile_pos, board):
        print('bishop')


class Queen(Piece):
    def get_available_moves(self, tile_pos, board):
        print('queen')


class King(Piece):
    def get_available_moves(self, tile_pos, board):
        print('king')

def tile_occupied_check(board, available_moves):
    for row in board:
        for tile in row:
            if tile.get_piece() is not None and tile.get_position() in available_moves:
                available_moves.remove(tile.get_position())
    return available_moves