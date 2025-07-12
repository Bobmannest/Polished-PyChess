import pygame


class Piece:
    def __init__(self, type: str):
        self.type = type

    def get_available_moves(self, temp_piece, tile_pos, board):
        # Optional: raise NotImplementedError to force subclasses to implement this
        raise NotImplementedError('Use subclass versions!')

    def get_type(self):
        return self.type


class Pawn(Piece):
    def get_available_moves(self,temp_piece, tile_pos, board):
        available_moves = []
        row, tile = tile_pos
        if 'wt' in self.type:
            available_moves.append([row - 1, tile])
        elif 'bk' in self.type:
            available_moves.append([row + 1, tile])
        return remove_occupied_tile_positions(board, available_moves)


class Rook(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []

        rook_available_moves(available_moves, temp_piece, tile_pos, board)

        return available_moves


class Knight(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
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

        return remove_occupied_tile_positions(board, available_moves)


class Bishop(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []

        bishop_available_moves(available_moves, tile_pos, board)

        return available_moves


class Queen(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        print('queen')


class King(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []
        row, tile = tile_pos

        r = row + 1
        for _ in range(2):
            t = tile - 1
            for _ in range(3):
                available_moves.append([r, t])
                t += 1
            r = row - 1
        available_moves.append([row, tile - 1]), available_moves.append([row, tile + 1])

        return remove_occupied_tile_positions(board, available_moves)

#I will probably make this less spaghetti later
def rook_available_moves(available_moves, temp_piece, tile_pos, board):
    row, tile = tile_pos

    t = tile - 1
    while t >= 0 and board[row][t].get_piece() is None:
        available_moves.append([row, t])
        t -= 1
    if board[row][t].get_piece() is not None and opposite_side(temp_piece, board[row][t].get_piece()):
        available_moves.append([row, t])
    t = tile + 1
    while t <= 7 and board[row][t].get_piece() is None:
        available_moves.append([row, t])
        t += 1
    if t <= 7 and board[row][t].get_piece() is not None and opposite_side(temp_piece, board[row][t].get_piece()):
        available_moves.append([row, t])
    r = row - 1
    t = tile
    while r >= 0 and board[r][t].get_piece() is None:
        available_moves.append([r, t])
        r -= 1
    if board[r][t].get_piece() is not None and opposite_side(temp_piece, board[r][t].get_piece()):
        available_moves.append([r, t])
    r = row + 1
    while r <= 7 and board[r][t].get_piece() is None:
        available_moves.append([r, t])
        r += 1
    if r <= 7 and board[r][t].get_piece() is not None and opposite_side(temp_piece, board[r][t].get_piece()):
        available_moves.append([r, t])


def bishop_available_moves(available_moves, tile_pos, board):
    row, tile = tile_pos

    r = row - 1
    t = tile - 1
    r2 = row + 1
    t2 = tile - 1
    while t >= 0:
        available_moves.append([r, t])
        available_moves.append([r2, t2])
        r -= 1
        t -= 1
        r2 += 1
        t2 -= 1

    r = row - 1
    t = tile + 1
    r2 = row + 1
    t2 = tile + 1
    while t <= 7:
        available_moves.append([r, t])
        available_moves.append([r2, t2])
        r -= 1
        t += 1
        r2 += 1
        t2 += 1


def remove_occupied_tile_positions(board, available_moves):
    for row in board:
        for tile in row:
            if tile.get_piece() is not None and tile.get_position() in available_moves:
                available_moves.remove(tile.get_position())
    return available_moves

def opposite_side(current_piece, target_piece):
    if 'wt' in current_piece.get_type() and 'bk' in target_piece.get_type():
        return True
    elif 'bk' in current_piece.get_type() and 'wt' in target_piece.get_type():
        return True
    else:
        return False
