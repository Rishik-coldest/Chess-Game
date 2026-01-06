import sys
import pygame

from Boardstate import BoardState, Move
from AIcode import RandomMove, alpha_beta_caller

pygame.init()

def fact_image(image, sfactor):
    size = round(image.get_width() * sfactor), round(image.get_height() * sfactor)
    newsize = pygame.transform.scale(image, size)
    return newsize

BOARD = pygame.image.load("Chessboard_green_squares.png")
MENU_BG = pygame.image.load("menuBG.jpg")
MENU_BG = fact_image(MENU_BG, 1.7887)
BLACK_BUTTON = pygame.image.load("black button.jpg")
BLACK_BUTTON  = fact_image(BLACK_BUTTON, 0.6)


#Width and height of screen
WIDTH = BOARD.get_width()
HEIGHT = (BOARD.get_height()) + 500
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))

FONT = pygame.font.SysFont("arileblack", 38)

class Button():
	def __init__(self, image, pos, text_input, font):
		self.image = image
		self.x_pos, self.y_pos = pos[0], pos[1]
		self.font = font
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, "white")
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

def main_menu():
    pygame.display.set_caption("Menu")
    run = True

    while run:
        SCREEN.blit(MENU_BG, (0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        TEXT = FONT.render("Main menu", True, "white")
        MENU_RECT = TEXT.get_rect(center=(400, 30))

        PLAY_OP_BTN = Button(image=BLACK_BUTTON, pos=(400, 120), text_input="VS Player", font=FONT)

        PLAY_VERY_EASY_AI_BTN = Button(image=BLACK_BUTTON, pos=(400, 230), text_input="VS Very Easy AI", font=FONT)

        PLAY_EASY_BTN = Button(image=BLACK_BUTTON, pos=(400, 340), text_input="VS Easy AI", font=FONT)

        PLAY_MEDIUM_BTN = Button(image=BLACK_BUTTON, pos=(400, 450), text_input="VS Medium AI", font=FONT)

        PLAY_HARD_BTN = Button(image=BLACK_BUTTON, pos=(400, 560), text_input="VS Hard AI", font=FONT)

        PLAY_VERY_HARD_BTN = Button(image=BLACK_BUTTON, pos=(400, 670), text_input="VS Very hard AI", font=FONT)

        QUIT_BTN = Button(image=BLACK_BUTTON, pos=(400, 780), text_input="QUIT", font=FONT)

        SCREEN.blit(TEXT, MENU_RECT)

        BTNs = [PLAY_VERY_EASY_AI_BTN, PLAY_OP_BTN, QUIT_BTN, PLAY_EASY_BTN, PLAY_MEDIUM_BTN, PLAY_HARD_BTN, PLAY_VERY_HARD_BTN]

        for button in BTNs:
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_VERY_EASY_AI_BTN.checkForInput(MENU_MOUSE_POS):
                    Very_Easy()
                if PLAY_OP_BTN.checkForInput(MENU_MOUSE_POS):
                    play_player()
                if PLAY_EASY_BTN.checkForInput(MENU_MOUSE_POS):
                    Easy()
                if PLAY_MEDIUM_BTN.checkForInput(MENU_MOUSE_POS):
                    Medium()
                if PLAY_HARD_BTN.checkForInput(MENU_MOUSE_POS):
                    Hard()
                if PLAY_VERY_HARD_BTN.checkForInput(MENU_MOUSE_POS):
                    Very_Hard()
                if QUIT_BTN.checkForInput(MENU_MOUSE_POS):
                    pygame.quit() 
                    sys.exit()

        pygame.display.update()

def are_you_sure():
    pygame.display.set_caption("Are you sure?")
    run = True

    while run:
        SCREEN.blit(MENU_BG, (0,0))
        are_you_sure_mouse_pos = pygame.mouse.get_pos()
        YES = Button(image=BLACK_BUTTON, pos=(400, 440), text_input="Yes", font=FONT)
        NO = Button(image=BLACK_BUTTON, pos=(700, 440), text_input="No", font=FONT)

        BTNs =[YES, NO]
        for button in BTNs:
            button.update(SCREEN)

        TEXT = FONT.render("Are you sure ?", True, "white")
        MENU_RECT = TEXT.get_rect(center=(550, 340))
        
        SCREEN.blit(TEXT, MENU_RECT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if YES.checkForInput(are_you_sure_mouse_pos):
                    main_menu()
                if NO.checkForInput(are_you_sure_mouse_pos):
                    return
        
        pygame.display.update()

def play_player():

    pygame.display.set_caption("Playing vs AI")
    G.opponent_mode()

def Very_Easy():

    pygame.display.set_caption("Playing vs Player")
    G.very_easy()

def Easy():

    pygame.display.set_caption("EasyAI")
    G.Easy_mode()

def Medium():

    pygame.display.set_caption("Hard mode")
    G.Medium_mode()
   
def Hard():
    
    pygame.display.set_caption("Time")
    G.Hard_mode()

def Very_Hard():
     
    pygame.display.set_caption("Saved game list")
    G.Very_Hard_mode()



class game():
    def __init__(self):
        self.Piece_imgs = {}
        self.screen = pygame.display.set_mode((900, 900))
        BOARD = pygame.image.load("Chessboard_green_squares.png")
        self.BOARD = pygame.transform.scale(BOARD, (900, 900))
        self.clicked_square = ()
        self.mouse_coords = []
        self.game_over = False
        self.boardstate = BoardState()
        self.Valid_moves = self.boardstate.vaild_moves()
        self.move_made = False
        pieces = ['wpawn', 'wrook', 'wknight', 'wbishop', 'wking', 'wqueen', 'bpawn', 'brook', 'bknight', 'bbishop', 'bking', 'bqueen']
        for piece in pieces:
            self.Piece_imgs[piece] = pygame.transform.scale(pygame.image.load(piece +  ".png"), (112, 112))
    
    def clear(self):
        self.clicked_square = () # deselect
        self.mouse_coords = [] # clear clicks
    
    def opponent_mode(self):
        run = True
        while run:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()  # (x, y) mouse_pos of the mouse
                        col = mouse_pos[0] // 112
                        row = mouse_pos[1] // 112
                        if self.clicked_square == (row, col) or col >= 8:  # user clicked the same square twice
                            self.clear()
                        else:
                            self.clicked_square = (row, col)
                            self.mouse_coords.append(self.clicked_square)  # append for both 1st and 2nd click
                        if len(self.mouse_coords) == 2:  # after 2nd click
                            move = Move(self.mouse_coords[0], self.mouse_coords[1], self.boardstate.board)
                            for i in range(len(self.Valid_moves)):
                                if move == self.Valid_moves[i]:
                                    self.boardstate.makeMove(self.Valid_moves[i]) 
                                    self.move_made = True
                                    self.clear()
                            if self.move_made == False:
                                self.mouse_coords = [self.clicked_square]
                            for i in self.boardstate.board:
                                print(i)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        are_you_sure()

                #AI move finder logic
                if not self.game_over:
                    self.move_made = True

                if self.move_made:
                    self.Valid_moves = self.boardstate.vaild_moves()
                    self.move_made = False
            
            self.screen.blit(self.BOARD, (0,0))
            for r in range(8):
                for c in range(8):
                    piece = self.boardstate.board[r][c]
                    if piece != "--":
                        self.screen.blit(self.Piece_imgs[piece], pygame.Rect(c*112, r*112, 112, 112))
                
            pygame.display.flip()

    def very_easy(self):
        run = True
        while run:
            if self.boardstate.player_1_move == True:
                player_turn = True
            elif self.boardstate.player_1_move == False:
                player_turn = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and player_turn:#added human turn here
                        mouse_pos = pygame.mouse.get_pos()  # (x, y) mouse_pos of the mouse
                        col = mouse_pos[0] // 112
                        row = mouse_pos[1] // 112
                        if self.clicked_square == (row, col) or col >= 8:  # user clicked the same square twice
                            self.clear()
                        else:
                            self.clicked_square = (row, col)
                            self.mouse_coords.append(self.clicked_square)  # append for both 1st and 2nd click
                        if len(self.mouse_coords) == 2:  # after 2nd click
                            move = Move(self.mouse_coords[0], self.mouse_coords[1], self.boardstate.board)
                            for i in range(len(self.Valid_moves)):
                                if move == self.Valid_moves[i]:
                                    self.boardstate.makeMove(self.Valid_moves[i]) 
                                    self.move_made = True
                                    self.clear()
                            if self.move_made == False:
                                self.mouse_coords = [self.clicked_square]
                            for i in self.boardstate.board:
                                print(i)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        are_you_sure()

                #AI move finder logic
                if not self.game_over and player_turn == False:
                    self.boardstate.makeMove(RandomMove(self.Valid_moves))
                    self.move_made = True

                if self.move_made:
                    self.Valid_moves = self.boardstate.vaild_moves()
                    self.move_made = False
            
            self.screen.blit(self.BOARD, (0,0))
            for r in range(8):
                for c in range(8):
                    piece = self.boardstate.board[r][c]
                    if piece != "--":
                        self.screen.blit(self.Piece_imgs[piece], pygame.Rect(c*112, r*112, 112, 112))
                
            pygame.display.flip()
    
    def Easy_mode(self):       
        run = True
        while run:
            if self.boardstate.player_1_move == True:
                player_turn = True
            elif self.boardstate.player_1_move == False:
                player_turn = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and player_turn:#added human turn here
                        mouse_pos = pygame.mouse.get_pos()  # (x, y) mouse_pos of the mouse
                        col = mouse_pos[0] // 112
                        row = mouse_pos[1] // 112
                        if self.clicked_square == (row, col) or col >= 8:  # user clicked the same square twice
                            self.clear()
                        else:
                            self.clicked_square = (row, col)
                            self.mouse_coords.append(self.clicked_square)  # append for both 1st and 2nd click
                        if len(self.mouse_coords) == 2:  # after 2nd click
                            move = Move(self.mouse_coords[0], self.mouse_coords[1], self.boardstate.board)
                            for i in range(len(self.Valid_moves)):
                                if move == self.Valid_moves[i]:
                                    self.boardstate.makeMove(self.Valid_moves[i]) 
                                    self.move_made = True
                                    self.clear()
                            if self.move_made == False:
                                self.mouse_coords = [self.clicked_square]
                            for i in self.boardstate.board:
                                print(i)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        are_you_sure()

                #AI move finder logic
                if not self.game_over and player_turn == False:
                    self.boardstate.makeMove(alpha_beta_caller(self.boardstate, self.Valid_moves, 2))
                    self.move_made = True

                if self.move_made:
                    self.Valid_moves = self.boardstate.vaild_moves()
                    self.move_made = False
            
            self.screen.blit(self.BOARD, (0,0))
            for r in range(8):
                for c in range(8):
                    piece = self.boardstate.board[r][c]
                    if piece != "--":
                        self.screen.blit(self.Piece_imgs[piece], pygame.Rect(c*112, r*112, 112, 112))
                
            pygame.display.flip()
    
    def Medium_mode(self):
        run = True
        while run:
            if self.boardstate.player_1_move == True:
                player_turn = True
            elif self.boardstate.player_1_move == False:
                player_turn = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and player_turn:#added human turn here
                        mouse_pos = pygame.mouse.get_pos()  # (x, y) mouse_pos of the mouse
                        col = mouse_pos[0] // 112
                        row = mouse_pos[1] // 112
                        if self.clicked_square == (row, col) or col >= 8:  # user clicked the same square twice
                            self.clear()
                        else:
                            self.clicked_square = (row, col)
                            self.mouse_coords.append(self.clicked_square)  # append for both 1st and 2nd click
                        if len(self.mouse_coords) == 2:  # after 2nd click
                            move = Move(self.mouse_coords[0], self.mouse_coords[1], self.boardstate.board)
                            for i in range(len(self.Valid_moves)):
                                if move == self.Valid_moves[i]:
                                    self.boardstate.makeMove(self.Valid_moves[i])
                                    self.move_made = True
                                    self.clear()
                            if self.move_made == False:
                                self.mouse_coords = [self.clicked_square]
                            for i in self.boardstate.board:
                                print(i)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        are_you_sure()

                #AI move finder logic
                if not self.game_over and player_turn == False:
                    self.boardstate.makeMove(alpha_beta_caller(self.boardstate, self.Valid_moves, 3))
                    self.move_made = True

                if self.move_made:
                    self.Valid_moves = self.boardstate.vaild_moves()
                    self.move_made = False
            
            self.screen.blit(self.BOARD, (0,0))
            for r in range(8):
                for c in range(8):
                    piece = self.boardstate.board[r][c]
                    if piece != "--":
                        self.screen.blit(self.Piece_imgs[piece], pygame.Rect(c*112, r*112, 112, 112))
                
            pygame.display.flip()
    
    def Hard_mode(self):    
        run = True
        while run:
            if self.boardstate.player_1_move == True:
                player_turn = True
            elif self.boardstate.player_1_move == False:
                player_turn = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and player_turn:#added human turn here
                        mouse_pos = pygame.mouse.get_pos()  # (x, y) mouse_pos of the mouse
                        col = mouse_pos[0] // 112
                        row = mouse_pos[1] // 112
                        if self.clicked_square == (row, col) or col >= 8:  # user clicked the same square twice
                            self.clear()
                        else:
                            self.clicked_square = (row, col)
                            self.mouse_coords.append(self.clicked_square)  # append for both 1st and 2nd click
                        if len(self.mouse_coords) == 2:  # after 2nd click
                            move = Move(self.mouse_coords[0], self.mouse_coords[1], self.boardstate.board)
                            for i in range(len(self.Valid_moves)):
                                if move == self.Valid_moves[i]:
                                    self.boardstate.makeMove(self.Valid_moves[i]) 
                                    self.move_made = True
                                    self.clear()
                            if self.move_made == False:
                                self.mouse_coords = [self.clicked_square]
                            for i in self.boardstate.board:
                                print(i)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        are_you_sure()

                #AI move finder logic
                if not self.game_over and player_turn == False:
                    self.boardstate.makeMove(alpha_beta_caller(self.boardstate, self.Valid_moves, 4))
                    self.move_made = True

                if self.move_made:
                    self.Valid_moves = self.boardstate.vaild_moves()
                    self.move_made = False
            
            self.screen.blit(self.BOARD, (0,0))
            for r in range(8):
                for c in range(8):
                    piece = self.boardstate.board[r][c]
                    if piece != "--":
                        self.screen.blit(self.Piece_imgs[piece], pygame.Rect(c*112, r*112, 112, 112))
                
            pygame.display.flip()
    
    def Very_Hard_mode(self):
        run = True
        while run:
            if self.boardstate.player_1_move == True:
                player_turn = True
            elif self.boardstate.player_1_move == False:
                player_turn = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and player_turn:#added human turn here
                        mouse_pos = pygame.mouse.get_pos()  # (x, y) mouse_pos of the mouse
                        col = mouse_pos[0] // 112
                        row = mouse_pos[1] // 112
                        if self.clicked_square == (row, col) or col >= 8:  # user clicked the same square twice
                            self.clear()
                        else:
                            self.clicked_square = (row, col)
                            self.mouse_coords.append(self.clicked_square)  # append for both 1st and 2nd click
                        if len(self.mouse_coords) == 2:  # after 2nd click
                            move = Move(self.mouse_coords[0], self.mouse_coords[1], self.boardstate.board)
                            for i in range(len(self.Valid_moves)):
                                if move == self.Valid_moves[i]:
                                    self.boardstate.makeMove(self.Valid_moves[i]) 
                                    self.move_made = True
                                    self.clear()
                            if self.move_made == False:
                                self.mouse_coords = [self.clicked_square]
                            for i in self.boardstate.board:
                                print(i)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        are_you_sure()

                #AI move finder logic
                if not self.game_over and player_turn == False:
                    self.boardstate.makeMove(alpha_beta_caller(self.boardstate, self.Valid_moves, 5))
                    self.move_made = True

                if self.move_made:
                    self.Valid_moves = self.boardstate.vaild_moves()
                    self.move_made = False
            
            self.screen.blit(self.BOARD, (0,0))
            for r in range(8):
                for c in range(8):
                    piece = self.boardstate.board[r][c]
                    if piece != "--":
                        self.screen.blit(self.Piece_imgs[piece], pygame.Rect(c*112, r*112, 112, 112))
                
            pygame.display.flip()

G = game()
if __name__ == "__main__":
   main_menu()
