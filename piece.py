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
            if tile > 0:
                pawn_move_calc(board[row - 1][tile - 1], temp_piece, available_moves)
            if tile < 7:
                pawn_move_calc(board[row - 1][tile + 1], temp_piece, available_moves)
        elif 'bk' in self.type:
            if board[row + 1][tile].get_piece() is None:
                available_moves.append([row + 1, tile])
            if tile > 0:
                pawn_move_calc(board[row + 1][tile - 1], temp_piece, available_moves)
            if tile < 7:
                pawn_move_calc(board[row + 1][tile + 1], temp_piece, available_moves)
        return available_moves

    def get_attack_moves(self, temp_piece, tile_pos, board):
        attack_moves = []
        row, tile = tile_pos
        if 'wt' in self.type:
            if tile > 0:
                attack_moves.append([row - 1, tile - 1])
            if tile < 7:
                attack_moves.append([row - 1, tile + 1])
        elif 'bk' in self.type:
            if tile > 0:
                attack_moves.append([row + 1, tile - 1])
            if tile < 7:
                attack_moves.append([row + 1, tile + 1])
        return attack_moves


def pawn_move_calc(tile, temp_piece, available_moves):
    if tile.get_piece() is not None:
        if opposite_side(temp_piece, tile.get_piece()):
            available_moves.append(tile.get_position())


class Rook(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []

        line_move_calc(available_moves, temp_piece, tile_pos, board, [[0, -1], [0, 1], [1, 0], [-1, 0]])

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

        return check_occupied_tile_positions(board, temp_piece, available_moves)


class Bishop(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []

        line_move_calc(available_moves, temp_piece, tile_pos, board, [[-1, -1], [-1, 1], [1, -1], [1, 1]])

        return available_moves


class Queen(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        available_moves = []

        line_move_calc(available_moves, temp_piece, tile_pos, board, [[0, -1], [0, 1], [1, 0], [-1, 0]])
        line_move_calc(available_moves, temp_piece, tile_pos, board, [[-1, -1], [-1, 1], [1, -1], [1, 1]])
        return available_moves


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
        check_occupied_tile_positions(board, temp_piece, available_moves)

        return check_king_available_moves(temp_piece, board, available_moves)


def check_king_available_moves(temp_piece, board, available_moves):
    safe_moves = available_moves.copy()
    bad_moves = []
    for row in board:
        for tile in row:
            tile_piece = tile.get_piece()
            if tile_piece is not None and 'king' not in tile_piece.get_type():
                if 'pawn' not in tile_piece.get_type():
                    if opposite_side(temp_piece, tile_piece):
                        bad_moves.append(tile_piece.get_available_moves(tile_piece, tile.get_position(), board))
                elif 'pawn' in tile_piece.get_type():
                    if opposite_side(temp_piece, tile_piece):
                        bad_moves.append(tile_piece.get_attack_moves(tile_piece, tile.get_position(), board))

    #Combines bad move sublists for each piece into 1 set of items
    all_bad_moves = set()
    for piece_moves in bad_moves:
        for move in piece_moves:
            all_bad_moves.add(tuple(move))

    #Creates a list of safe moves that removes bad moves from available_moves
    safe_moves = [move for move in safe_moves if tuple(move) not in all_bad_moves]

    return safe_moves

def check_occupied_tile_positions(board, temp_piece, available_moves):
    for row in board:
        for tile in row:
            if tile.get_piece() is not None and tile.get_position() in available_moves and not opposite_side(temp_piece,
                                                                                                             tile.get_piece()):
                available_moves.remove(tile.get_position())
    return available_moves


def line_move_calc(available_moves, temp_piece, tile_pos, board, increments):
    for position in increments:
        row, tile = tile_pos
        row += position[0]
        tile += position[1]
        while 0 <= row <= 7 and 0 <= tile <= 7:
            target_piece = board[row][tile].get_piece()
            if target_piece is None:
                available_moves.append([row, tile])
            elif target_piece is not None and opposite_side(temp_piece, target_piece):
                available_moves.append([row, tile])
                break
            elif target_piece is not None and not opposite_side(temp_piece, target_piece):
                break
            row += position[0]
            tile += position[1]


def opposite_side(current_piece, target_piece):
    if 'wt' in current_piece.get_type() and 'bk' in target_piece.get_type():
        return True
    elif 'bk' in current_piece.get_type() and 'wt' in target_piece.get_type():
        return True
    else:
        return False
