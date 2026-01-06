class Move:
    def __init__(self, startSq, endSq, board):
        self.startSq = startSq
        self.endSq = endSq
        self.board = board
        self.pieceMoved = board[self.startSq[0]][self.startSq[1]]
        self.pieceCaptured = board[self.endSq[0]][self.endSq[1]]
        self.move_code = self.startSq[0] * 1000 + self.startSq[1] * 100 + self.endSq[0] * 10 + self.endSq[1] #Like a hashing algorithm
        self.Promotion = False
        if self.pieceMoved == 'wpawn' and self.endSq[0] == 0:
            self.Promotion = True 
        if self.pieceMoved == 'bpawn' and self.endSq[0] == 7:
            self.Promotion = True

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_code == other.move_code
        return False