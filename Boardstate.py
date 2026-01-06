from Move_class import Move
from Pieces_class import Pieces


class BoardState(Pieces):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register = []
        self.check_mate = False
        self.stale_mate = False
        self.wking_square = (7, 4)
        self.bking_square = (0, 4)
        self.wl = self.wr = self.bl = self.br = True

    def record_king_square(self, move):
        if move.pieceMoved == 'wking':                                    
            self.wking_square = (move.endSq[0], move.endSq[1])             
        elif move.pieceMoved == 'bking':   
            self.bking_square = (move.endSq[0], move.endSq[1])
    
    def pawn_promotion(self, move):
        if move.Promotion:  
            self.board[move.endSq[0]][move.endSq[1]] = move.pieceMoved[0] + 'queen'
    
    def switch(self):
        self.player_1_move = not self.player_1_move

    def makeMove(self, move):
        self.board[move.startSq[0]][move.startSq[1]] = "--"
        self.board[move.endSq[0]][move.endSq[1]] = move.pieceMoved
        self.register.append(move)
        self.switch()            
        self.record_king_square(move)
        self.pawn_promotion(move)

        # Define a dictionary to map piece types to their castling flags
        castling_flags = {
            'wking': ('self.castling_check.white_right', 'self.castling_check.white_left'),
            'bking': ('self.castling_check.black_right', 'self.castling_check.black_left'),
            'wrook': {'startRow': 7, 'flags': {'0': 'self.castling_check.white_left', '7': 'self.castling_check.white_right'}},
            'brook': {'startRow': 0, 'flags': {'0': 'self.castling_check.black_left', '7': 'self.castling_check.black_right'}}
        }

        # Check if the piece type is in the castling flags dictionary
        if move.pieceMoved in castling_flags:
            # Handle king moves
            if move.pieceMoved in ['wking', 'bking']:
                for flag in castling_flags[move.pieceMoved]:
                    setattr(self, flag, False)
            # Handle rook moves
            elif move.pieceMoved in ['wrook', 'brook']:
                if move.startSq[0] == castling_flags[move.pieceMoved]['startRow']:
                    flag_key = str(move.startSq[1])
                    if flag_key in castling_flags[move.pieceMoved]['flags']:
                        flag_to_update = castling_flags[move.pieceMoved]['flags'][flag_key]
                        setattr(self, flag_to_update, False)




    def vaild_moves(self):
        
        pos_moves = self.possible_moves()

        for i in range(len(pos_moves)-1, -1, -1):
            self.makeMove(pos_moves[i])
            self.switch()
            if self.check():
                pos_moves.remove(pos_moves[i])
            self.switch()  
            #cycles through possibles moves to verify check and checkmate
            self.reverse_check()
            
        if len(pos_moves) == 0:
            if self.check():
                self.check_mate = True
            else:
                self.stale_mate = True
        else:
            self.check_mate = False
            self.stale_mate = False
        
        return pos_moves
    

    def reverse_check(self):
        if len(self.register) != 0:
                move = self.register.pop()
                self.board[move.startSq[0]][move.startSq[1]] = move.pieceMoved
                self.board[move.endSq[0]][move.endSq[1]] = move.pieceCaptured
                self.switch()
                
                king_squares = {'wking': 'wking_square', 'bking': 'bking_square'} # check if the piece moved is a king
                if move.pieceMoved in king_squares: # update the square accordingly
                    setattr(self, king_squares[move.pieceMoved], (move.endSq[0], move.endSq[1]))

                if move.pieceMoved[1:] == 'pawn' and (move.startSq[0] - move.endSq[0]) == 2:
                    self.enpassant = ()
                               
                self.check_mate = self.stale_mate = False


    def handle_castling(self, move):
        if move.endSq[1] - move.startSq[1] == 2:
            # Kingside castle
            rook_start_col = 7
            rook_end_col = 5
        else:
            # Queenside castle
            rook_start_col = 0
            rook_end_col = 3

        # Move the rook
        self.board[move.endSq[0]][rook_end_col] = self.board[move.endSq[0]][rook_start_col]
        self.board[move.endSq[0]][rook_start_col] = '--'


    def check(self):
        if self.player_1_move:
            return self.check_for_check(self.wking_square[0], self.wking_square[1])
        else:
            return self.check_for_check(self.bking_square[0], self.bking_square[1])
        
    def check_for_check(self, r, c):
        self.switch()
        enemy_moves = self.possible_moves()
        for move in enemy_moves:
            if move.endSq[0] == r and move.endSq[1] == c:
                self.switch()
                return True
        self.switch()

    def possible_moves(self):
        moves = []
        for r in range(8):
            for c in range(8):
                if (self.board[r][c][0] =='w' and self.player_1_move) or (self.board[r][c][0] == 'b' and not self.player_1_move):
                    if self.board[r][c][1:] == 'pawn':
                        self.Pawn_moves(r, c, moves)
                    elif self.board[r][c][1:] == 'knight':
                        self.knight_moves(r, c, moves)
                    elif self.board[r][c][1:] == 'bishop':
                        self.Bishop_moves(r, c, moves)
                    elif self.board[r][c][1:] == 'queen':
                        self.Queen_moves(r, c, moves)
                    elif self.board[r][c][1:] == 'king':
                        self.King_moves(r, c, moves)
                    elif self.board[r][c][1:] == 'rook':
                        self.Rook_moves(r, c, moves)
        return moves

    def castle_white_r(self):
        if self.wr == True:
            return True
    
    def castle_white_l(self):
        if self.wl == True:
            return True
    
    def castle_black_r(self):
        if self.br == True:
            return True
    
    def castle_black_l(self):
        if self.bl == True:
            return True

    
    def get_castle_moves(self, r, c, moves):
        if self.check_for_check(r, c):
            return
        
        if self.player_1_move and self.castle_white_r():
            for i in range(1, 3):
                if all(self.board[r][c+i] == '--') and not any(self.check_for_check(r, c+i) for i in range(1, 3)):
                    moves.append(Move((r, c), (r, c+2), self.board))
        if self.player_1_move == False and self.castle_black_r():
            for i in range(1, 3):
                if all(self.board[r][c+i] == '--') and not any(self.check_for_check(r, c+i) for i in range(1, 3)):
                    moves.append(Move((r, c), (r, c+2), self.board))
        if self.player_1_move and self.castle_white_l():
            for i in range(1, 4):
                if all(self.board[r][c-i] == '--') and not any(self.check_for_check(r, c-i) for i in range(1, 4)):
                    moves.append(Move((r, c), (r, c-2), self.board))
        if self.player_1_move == False and self.castle_black_l():
            for i in range(1, 4):
                if all(self.board[r][c-i] == '--') and not any(self.check_for_check(r, c-i) for i in range(1, 4)):
                    moves.append(Move((r, c), (r, c-2), self.board))
