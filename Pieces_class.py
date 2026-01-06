from Move_class import Move


class Pieces:
    def __init__(self):
        self.board = [
    ["brook", "bknight", "bbishop", "bqueen", "bking", "bbishop", "bknight", "brook"],
    ["bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn"],
    ["wrook", "wknight", "wbishop", "wqueen", "wking", "wbishop", "wknight", "wrook"]
    ]
        self.player_1_move = True
        self.enpassant = ()

    def Pawn_moves(self, r, c, moves):
        if self.player_1_move: # white pawn moves
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c), (r-1,c), self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r,c), (r-2,c), self.board))
            
            #capturing diganolly to the left 
            if c-1 >= 0:
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(Move((r,c), (r-1, c-1), self.board))
                elif (r-1, c-1) == self.enpassant:
                    moves.append(Move((r, c), (r-1, c-1), self.board))
            
            #capturing diagonolly to the right
            if c+1 <= 7:
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r,c), (r-1, c+1), self.board))
                elif (r-1, c+1) == self.enpassant:
                    moves.append(Move((r, c), (r-1, c+1), self.board))
            
        else: #black pawn moves
            if self.board[r+1][c] == "--":
                moves.append(Move((r,c), (r+1,c), self.board))
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(Move((r,c), (r+2,c), self.board))
                
                #capturing diagonally to the left
                if c-1 >= 0:
                    if self.board[r+1][c-1][0] == 'w':
                        moves.append(Move((r,c), (r+1, c-1), self.board))
                    elif (r+1, c-1) == self.enpassant:
                        moves.append(Move((r, c), (r+1, c-1), self.board))
                
                #capturing diaganally to the right
                if c+1 <= 7:
                    if self.board[r+1][c+1][0] == 'w':
                        moves.append(Move((r,c), (r+1, c+1), self.board))
                    elif (r+1, c+1) == self.enpassant:
                        moves.append(Move((r, c), (r+1, c+1), self.board))


    def Rook_moves(self, r, c, moves):     
        if self.player_1_move:
            enemyColor = 'b'
        else:
            enemyColor = 'w'
        for i in range(4):
            for j in range(1,8):
                if i == 0:
                    end = (-1, 0)
                elif i == 1:
                    end = (0, -1)
                elif i == 2:
                    end = (1, 0)
                elif i == 3:
                    end = (0, 1)

                start = (r, c)
                row = start[0] + (end[0] * j)
                col = start[1] + (end[1] * j)
                end = (row, col)
                if 0 <= row < 8 and 0 <= col < 8:
                    if self.board[row][col] == "--":
                        moves.append(Move((start), (end), self.board))
                    elif self.board[row][col][0] == enemyColor:
                        moves.append(Move((start), (end), self.board))
                        break
                    else:
                        break
                else:
                    break



    def knight_moves(self, r, c, moves):
        if self.player_1_move:
            enemy_colour = 'b'
        else:
            enemy_colour = 'w'
        start = (r,c)
        for move in range(8):
            if move == 0:
                end = (r-2, c-1)
            elif move == 1:
                end = (r-2, c+1)
            elif move == 2:
                end = (r-1, c+2)
            elif move == 3:
                end = (r+1, c+2)
            elif move == 4:
                end = (r+2, c+1)
            elif move == 5:
                end = (r+2, c-1)
            elif move == 6:
                end = (r+1, c-2)
            elif move == 7:
                end = (r-1, c-2)
            if (0 <= end[0] < 8 and 0 <= end[1] < 8) and (self.board[end[0]][end[1]][0] == enemy_colour or "--"):
                moves.append(Move((start), (end), self.board))
        

    def Bishop_moves(self, r, c, moves):
        if self.player_1_move:
            enemyColor = 'b'
        else:
            enemyColor = 'w'
        for i in range(4):
            for j in range(1,8):
                if i == 0:
                    end = (1, 1)
                elif i == 1:
                    end = (-1, 1)
                elif i == 2:
                    end = (-1, -1)
                elif i == 3:
                    end = (1, -1)

                start = (r, c)
                row = start[0] + (end[0] * j)
                col = start[1] + (end[1] * j)
                end = (row, col)
                if 0 <= end[0] < 8 and 0 <= end[1] < 8:
                    if self.board[end[0]][end[1]] == "--":
                        moves.append(Move((start), (end), self.board))
                    elif self.board[end[0]][end[1]][0] == enemyColor:
                        moves.append(Move((start), (end), self.board))
                        break
                    else:
                        break
                else:
                    break
        
        
    def Queen_moves(self, r, c, moves):
        self.Bishop_moves(r, c, moves)
        self.Rook_moves(r, c, moves)


    def King_moves(self, r, c, moves):

        if self.player_1_move:
            enemy_colour = 'b'
        else:
            enemy_colour = 'w'
        start = (r,c)
        for move in range(8):
            if move == 0:
                end = (r-1, c)
            elif move == 1:
                end = (r-1, c+1)
            elif move == 2:
                end = (r-1, c-1)
            elif move == 3:
                end = (r, c-1)
            elif move == 4:
                end = (r, c+1)
            elif move == 5:
                end = (r+1, c)
            elif move == 6:
                end = (r+1, c+1)
            elif move == 7:
                end = (r+1, c-1)
            if (0 <= end[0] < 8 and 0 <= end[1] < 8) and (self.board[end[0]][end[1]][0] == enemy_colour or "--"):
                moves.append(Move((start), (end), self.board))