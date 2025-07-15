class Piece:
    def __init__(self, type: str):
        self.type = type
        self.guarded = False

    def get_available_moves(self, temp_piece, tile_pos, board):
        # Optional: raise NotImplementedError to force subclasses to implement this
        raise NotImplementedError('Use subclass versions!')

    def get_type(self):
        return self.type

    def is_guarded(self):
        return self.guarded

    def set_guarded(self, guarded_status: bool):
        self.guarded = guarded_status


class Pawn(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        pawn_available_moves = []

        row, tile = tile_pos
        if 'wt' in self.type:
            if board[row - 1][tile].get_piece() is None:
                pawn_available_moves.append([row - 1, tile])
            if tile > 0:
                self.pawn_move_calc(board[row - 1][tile - 1], temp_piece, pawn_available_moves)
            if tile < 7:
                self.pawn_move_calc(board[row - 1][tile + 1], temp_piece, pawn_available_moves)
        elif 'bk' in self.type:
            if board[row + 1][tile].get_piece() is None:
                pawn_available_moves.append([row + 1, tile])
            if tile > 0:
                self.pawn_move_calc(board[row + 1][tile - 1], temp_piece, pawn_available_moves)
            if tile < 7:
                self.pawn_move_calc(board[row + 1][tile + 1], temp_piece, pawn_available_moves)

        return pawn_available_moves

    def get_attack_moves(self, tile_pos):
        pawn_attack_moves = []
        row, tile = tile_pos
        if 'wt' in self.type:
            if tile > 0:
                pawn_attack_moves.append([row - 1, tile - 1])
            if tile < 7:
                pawn_attack_moves.append([row - 1, tile + 1])
        elif 'bk' in self.type:
            if tile > 0:
                pawn_attack_moves.append([row + 1, tile - 1])
            if tile < 7:
                pawn_attack_moves.append([row + 1, tile + 1])
        return pawn_attack_moves


    def pawn_move_calc(self, tile, temp_piece, pawn_available_moves):
        if tile.get_piece() is not None:
            if opposite_side(temp_piece, tile.get_piece()):
                pawn_available_moves.append(tile.get_position())
            else:
                tile.get_piece().set_guarded(True)


class Rook(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        rook_available_moves = []

        line_move_calc(rook_available_moves, temp_piece, tile_pos, board, [[0, -1], [0, 1], [1, 0], [-1, 0]])

        return rook_available_moves


class Knight(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        knight_available_moves = []
        row, tile = tile_pos

        t = tile + 2
        knight_available_moves.append([row + 1, t]), knight_available_moves.append([row - 1, t])
        t = tile - 2
        knight_available_moves.append([row + 1, t]), knight_available_moves.append([row - 1, t])
        t = tile - 1
        knight_available_moves.append([row + 2, t]), knight_available_moves.append([row - 2, t])
        t = tile + 1
        knight_available_moves.append([row + 2, t]), knight_available_moves.append([row - 2, t])

        knight_available_moves = self.check_knight_occupied_tile_positions(board, temp_piece, knight_available_moves)

        return knight_available_moves

    def check_knight_occupied_tile_positions(self, board, temp_piece, knight_available_moves):
        for row in board:
            for tile in row:
                if tile.get_piece() is not None and tile.get_position() in knight_available_moves and not opposite_side(
                        temp_piece, tile.get_piece()):
                    knight_available_moves.remove(tile.get_position())
                    tile.get_piece().set_guarded(True)
        return knight_available_moves


class Bishop(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        bishop_available_moves = []

        line_move_calc(bishop_available_moves, temp_piece, tile_pos, board, [[-1, -1], [-1, 1], [1, -1], [1, 1]])

        return bishop_available_moves


class Queen(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        queen_available_moves = []

        line_move_calc(queen_available_moves, temp_piece, tile_pos, board, [[0, -1], [0, 1], [1, 0], [-1, 0]])
        line_move_calc(queen_available_moves, temp_piece, tile_pos, board, [[-1, -1], [-1, 1], [1, -1], [1, 1]])

        return queen_available_moves


# noinspection PyMethodMayBeStatic
class King(Piece):
    def get_available_moves(self, temp_piece, tile_pos, board):
        king_available_moves = []
        row, tile = tile_pos

        r = row + 1
        for _ in range(2):
            t = tile - 1
            for _ in range(3):
                king_available_moves.append([r, t])
                t += 1
            r = row - 1
        king_available_moves.append([row, tile - 1])
        king_available_moves.append([row, tile + 1])

        in_range_available_moves = remove_out_of_range_moves(king_available_moves)
        unoccupied_available_moves = self.check_king_occupied_tile_positions(board, temp_piece, in_range_available_moves)
        available_moves = self.check_guarded_moves(board, unoccupied_available_moves)

        return self.check_king_available_moves(temp_piece, board, available_moves)

    def check_king_occupied_tile_positions(self, board, temp_piece, king_available_moves):
        occupied_positions = []
        for move in king_available_moves:
            tile = board[move[0]][move[1]]
            if tile.get_piece() is not None:
                if tile.get_position() in king_available_moves and not opposite_side(temp_piece, tile.get_piece()):
                    occupied_positions.append(tile.get_position())
                    tile.get_piece().set_guarded(True)
        return [move for move in king_available_moves if move not in occupied_positions]

    def check_guarded_moves(self, board, king_available_moves):
        guarded_moves = []
        for move in king_available_moves:
            row, tile = move
            if board[row][tile].get_piece() is not None:
                if board[row][tile].get_piece().is_guarded():
                    guarded_moves.append([row, tile])
        return [move for move in king_available_moves if move not in guarded_moves]

    def check_king_available_moves(self, temp_piece, board, king_available_moves):
        safe_moves = king_available_moves.copy()
        bad_moves = []
        for row in board:
            for tile in row:
                tile_piece = tile.get_piece()
                if tile_piece is not None and 'king' not in tile_piece.get_type():
                    if 'pawn' not in tile_piece.get_type() and opposite_side(temp_piece, tile_piece):
                        bad_moves.append(tile_piece.get_available_moves(tile_piece, tile.get_position(), board))
                    elif 'pawn' in tile_piece.get_type() and opposite_side(temp_piece, tile_piece):
                        bad_moves.append(tile_piece.get_attack_moves(tile.get_position()))

        #Combines bad move sublists for each piece into 1 set of items
        all_bad_moves = set()
        for piece_moves in bad_moves:
            for move in piece_moves:
                all_bad_moves.add(tuple(move))

        #Creates a list of safe moves that removes bad moves from available_moves
        safe_moves = [move for move in safe_moves if tuple(move) not in all_bad_moves]
        return safe_moves


# Returns a new list of moves that have out of range moves filtered out of original available moves list
def remove_out_of_range_moves(available_moves):
    return [move for move in available_moves if all(row_or_tile < 8 for row_or_tile in move)]


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
                target_piece.set_guarded(True)
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
