import pygame


class Piece:
    def __init__(self, type: str):
        self.type = type

    def get_available_moves(self, temp_piece, tile_pos, board):
        # Optional: raise NotImplementedError to force subclasses to implement this
        raise NotImplementedError('Use subclass versions!')

    def get_type(self):
        return self.type


#Fix spaghetti with some nice functions which take +1 or -1 as input
class Pawn(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []
        row, tile = tile_pos
        if 'wt' in self.type:
            if board[row - 1][tile].get_piece() is None:
                available_moves.append([row - 1, tile])
            pawn_move_calc(board[row - 1][tile - 1], temp_piece, available_moves)
            pawn_move_calc(board[row - 1][tile + 1], temp_piece, available_moves)
        elif 'bk' in self.type:
            if board[row + 1][tile].get_piece() is None:
                available_moves.append([row + 1, tile])
            pawn_move_calc(board[row + 1][tile - 1], temp_piece, available_moves)
            pawn_move_calc(board[row + 1][tile + 1], temp_piece, available_moves)
        return available_moves


def pawn_move_calc(tile, temp_piece, available_moves):
    if tile.get_piece() is not None:
        if opposite_side(temp_piece, tile.get_piece()):
            available_moves.append(tile.get_position())


class Rook(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []

        rook_available_moves(available_moves, temp_piece, tile_pos, board)

        return available_moves


def rook_available_moves(available_moves, temp_piece, tile_pos, board):
    row, tile = tile_pos

    tile_L = tile - 1
    for _ in range(tile):
        if board[row][tile_L].get_piece() is None:
            available_moves.append([row, tile_L])
            tile_L -= 1
        elif board[row][tile_L].get_piece() is not None and opposite_side(temp_piece, board[row][tile_L].get_piece()):
            available_moves.append([row, tile_L])


    tile_R = tile + 1
    for _ in range(7 - tile):
        if board[row][tile_R].get_piece() is None:
            available_moves.append([row, tile_R])
            tile_R += 1
        elif board[row][tile_R].get_piece() is not None and opposite_side(temp_piece, board[row][tile_R].get_piece()):
            available_moves.append([row, tile_R])

    row_U = row - 1
    for _ in range(row):
        if board[row_U][tile].get_piece() is None:
            available_moves.append([row_U, tile])
            row_U -= 1
        elif board[row_U][tile].get_piece() is not None and opposite_side(temp_piece, board[row_U][tile].get_piece()):
            available_moves.append([row_U, tile])

    row_D = row + 1
    for _ in range(7 - row):
        if board[row_D][tile].get_piece() is None:
            available_moves.append([row_D, tile])
            row_D += 1
        elif board[row_D][tile].get_piece() is not None and opposite_side(temp_piece, board[row_D][tile].get_piece()):
            available_moves.append([row_D, tile])



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

#Make less spaghetti garbage
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


def remove_out_of_range_positions(board, available_moves):
    for row in board:
        for tile in row:
            if tile.get_position()[0] < 0 or tile.get_position()[0] > 7:
                print('e')

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
