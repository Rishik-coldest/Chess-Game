import random

value = {"king": 0, "queen": 10, "rook": 5, "bishop": 3, "knight": 3, "pawn": 1}
Checkmate = 1000
Stalemate = 0

def scorematerial(board):
    score = 0
    for r in board:
        for square in r:
            if square[0] == 'w':
                score = score + value[square[1:]]
            elif square[0] == 'b':
                score = score - value[square[1:]]
    return score


#Easy mode
def RandomMove(Valid_moves):
    return Valid_moves[random.randint(0, len(Valid_moves)-1)]

def Min_max_no_recursion(gs, vaild_moves): # Minmax with depth of 2
    if gs.player_1_move:
        turnchecker = 1
    else:
        turnchecker = -1
    opp_minmax_score = Checkmate
    Best_player_move = None
    for i in range(len(vaild_moves)):
        random_index = random.randint(0, len(vaild_moves) - 1)
        vaild_moves[i] = vaild_moves[random_index]
        vaild_moves[random_index] = vaild_moves[i]
    for playermove in vaild_moves:
        gs.makeMove(playermove)
        opponentMoves = gs.vaild_moves()  # valid_moves eror
        if gs.stale_mate:
            opp_max_score = Stalemate
        elif gs.check_mate:
            opp_max_score = -Checkmate
        else:
            opp_max_score = -Checkmate
            for oppMove in opponentMoves:
                gs.makeMove(oppMove)
                gs.vaild_moves()
                if gs.check_mate:
                    score = turnchecker * Checkmate
                elif gs.check_mate:
                    score = 0
                else:
                    score = -turnchecker * scorematerial(gs.board)
                if score > opp_max_score:
                    opp_max_score = score
                gs.reverse_check()
            if opp_max_score < opp_minmax_score:
                opp_minmax_score = opp_max_score
                Best_player_move = playermove
            gs.reverse_check()
        return Best_player_move

def min_max_caller(gs, validmoves, Depth):
    global nextMove
    nextMove = None#maybe not needed
    for i in range(len(validmoves)):
        random_index = random.randint(0, len(validmoves) - 1)
        validmoves[i] = validmoves[random_index]
        validmoves[random_index] = validmoves[i]
        MaxDepth = Depth
    Min_Max(gs, validmoves, Depth, gs.player_1_move, MaxDepth)
    return nextMove

def nega_max_caller(gs, validmoves, Depth):
    global nextMove
    nextMove = None#maybe not needed
    for i in range(len(validmoves)):
        random_index = random.randint(0, len(validmoves) - 1)
        validmoves[i] = validmoves[random_index]
        validmoves[random_index] = validmoves[i]
    if gs.player_1_move:
        turncheck = 1
    else:
        turncheck = -1
    MaxDepth = Depth
    nega_max(gs, validmoves, Depth, turncheck, MaxDepth)
    return nextMove

def Min_Max(gs, validmoves, depth, player_1_move, MaxDepth):
    global nextMove
    if depth == 0:
        return scorematerial(gs.board)
    
    if player_1_move:
        maxScore = -Checkmate
        for move in validmoves:
            gs.makeMove(move)
            nextmoves = gs.vaild_moves()
            score = Min_Max(gs,nextmoves, depth-1, not player_1_move)
            if score > maxScore:
                maxScore = score
                if depth == MaxDepth:
                    nextMove = move
            gs.reverse_check()
        return maxScore
    else:
        minScore = Checkmate
        for move in validmoves:
            gs.makeMove(move)
            nextmoves = gs.vaild_moves()
            score = Min_Max(gs, nextmoves, depth-1, player_1_move)
            if score < minScore:
                minScore = score
                if depth == MaxDepth:
                    nextMove = move
            gs.reverse_check()
        return minScore


def nega_max(gs, validmoves, depth, turnchecker, MaxDepth):
    global nextMove
    if depth == 0: #base case
        return turnchecker * scoreboard(gs)
    
    maxScore = -Checkmate
    for move in validmoves:
        gs.makeMove(move)
        nextmoves = gs.vaild_moves()
        score = -nega_max(gs, nextmoves, depth-1, -turnchecker)
        if score > maxScore:
            maxScore = score
            if depth == MaxDepth:
                nextMove = move
        gs.reverse_check()
    return maxScore

def alpha_beta_caller(gs, validmoves, Depth):
    global nextMove
    nextMove = None#maybe not needed
    for i in range(len(validmoves)):
        random_index = random.randint(0, len(validmoves) - 1)
        validmoves[i] = validmoves[random_index]
        validmoves[random_index] = validmoves[i]
    if gs.player_1_move:
        turncheck = 1
    else:
        turncheck = -1
    MaxDepth = Depth
    alpha_beta_pruning(gs, validmoves, Depth, turncheck, -Checkmate, Checkmate, MaxDepth)
    return nextMove


def alpha_beta_pruning(gs, validmoves, depth, turnchecker, alpha, beta, MaxDepth): 
    global nextMove
    if depth == 0: #base case
        return turnchecker * scoreboard(gs)
    
    #order the moves
    maxScore = -Checkmate
    for move in validmoves:
        gs.makeMove(move)
        nextmoves = gs.vaild_moves()
        score = -alpha_beta_pruning(gs, nextmoves, depth-1, -turnchecker, -alpha, -beta, MaxDepth)
        if score > maxScore:
            maxScore = score
            if depth == MaxDepth:
                nextMove = move
        gs.reverse_check()
        alpha = max(maxScore, alpha)
        if alpha >= beta:
            break
    return maxScore

def scoreboard(gs):
    if gs.check_mate:
        if gs.player_1_move:
            return -Checkmate #black wins
        else:
            return Checkmate #white wins
    elif gs.stale_mate:
        return Stalemate
    score = 0
    for r in range(8):
        for c in range(len(gs.board[r])):
            square = gs.board[r][c]
            if square != "--":

                if square[1:] == "king":
                    King = [[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
        [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0], 
        [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0], 
        [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0], 
        [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]]
                    if square[0] == 'w':
                        piece = King[r][c]
                        score = score + value[square[1:]] + piece
                    elif square[0] == 'b':
                        King = [row[::-1] for row in King[::-1]] # flips the entire array
                        piece = King[r][c]
                        score = score - value[square[1:]] + piece
                        King = [row[::-1] for row in King[::-1]]
                
                if square[1:] == "queen":
                    Queen = [[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
         [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
         [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
         [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
         [ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
         [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
         [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
         [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]
                    if square[0] =='w':
                        piece = Queen[r][c]
                        score = score + value[square[1:]] + piece
                    elif square[0] == 'b':
                        Queen = [row[::-1] for row in Queen[::-1]]
                        piece = Queen[r][c]
                        score = score - value[square[1:]] + piece
                        Queen = [row[::-1] for row in Queen[::-1]]
                
                if square[1:] == "bishop":
                    Bishop = [[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0], 
          [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0], 
          [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0], 
          [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0], 
          [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0], 
          [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0], 
          [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0], 
          [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
                    if square[0] =='w':
                        piece = Bishop[r][c]
                        score = score + value[square[1:]] + piece
                    elif square[0] == 'b':
                        Bishop = [row[::-1] for row in Bishop[::-1]]
                        piece = Bishop[r][c]
                        score = score - value[square[1:]] + piece
                        Bishop = [row[::-1] for row in Bishop[::-1]]
                
                if square[1:] == "knight":
                    Knight = [[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0], 
                              [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0], 
                              [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0], 
                              [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0], 
                              [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0], 
                              [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0], 
                              [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0], 
                              [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
                    if square[0] =='w':
                        piece = Knight[r][c]
                        score = score + value[square[1:]] + piece
                    elif square[0] == 'b':
                        Knight = [row[::-1] for row in Knight[::-1]]
                        piece = Knight[r][c]
                        score = score - value[square[1:]] + piece
                        Knight = [row[::-1] for row in Knight[::-1]]

                if square[1:] == "pawn":
                    Pawn = [[ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0], 
        [ 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0], 
        [ 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0], 
        [ 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5], 
        [ 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0], 
        [ 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5], 
        [ 0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5], 
        [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]
                    if square[0] =='w':
                        piece = Pawn[r][c]
                        score = score + value[square[1:]] + piece
                    elif square[0] == 'b':
                        Pawn = [row[::-1] for row in Pawn[::-1]]
                        piece = Pawn[r][c]
                        score = score - value[square[1:]] + piece
                        Pawn = [row[::-1] for row in Pawn[::-1]]

                if square[1:] == "rook":
                    Rook = [[ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0], 
        [ 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5], 
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5], 
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5], 
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5], 
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5], 
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5], 
        [ 0.5,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.5]]
                    if square[0] =='w':
                        piece = Rook[r][c]
                        score = score + value[square[1:]] + piece
                    elif square[0] == 'b':
                        Rook = [row[::-1] for row in Rook[::-1]]
                        piece = Rook[r][c]
                        score = score - value[square[1:]] + piece
                        Rook = [row[::-1] for row in Rook[::-1]]

    return score
