from base_game import mouse_pos,Game,create_button
import pygame
import numpy as np
from datetime import datetime

class othello(Game):

    def __init__(self, players, current_player, surface, size):
        super().__init__(players, current_player, surface, size)
        self.still_playing = True
        self.board[3:5,3:5] = np.array([[2,1],[1,2]])                               # Initialising board with 2 whites and 2 blacks in center
        self.directions = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]           # Defining direction's of checking valid moves
        self.valid_moves(1)
        self.font = pygame.font.Font(None,52)
        self.ok_button = create_button("Ok",(255,255,255),self.font,self.surface.get_rect().centerx,600,80,300)
        self.results = {}                                                                       # Creating results dictionary
        
    def player_count(self,player):                                                  # Calculating player scores
        return np.where(self.board == player)[0].size

    def change_turn(self):                                                          # Changing turn
        return super().change_turn()
    
    def handle_click(self,mx,my):                                                   # Handlimg click using mouse position
        if self.still_playing:
            if not np.any(self.board == 3):                                         # Handling click for no moves for a single player
                if self.ok_button["button_pos"].collidepoint(mx,my):
                    self.change_turn()
                    self.valid_moves(self.current_player+1)
                    if not self.check_playing():
                        self.still_playing = False
                return
            for i in range(self.size):
                if 100+100*i < my < 200+100*i:
                    for j in range(self.size):
                        if 350+100*j<mx<450+100*j:
                            if self.board[i][j] == 3:
                                self.update_board(i,j)
                                if self.check_playing():                            # Checking for further possibilty of game
                                    self.change_turn()
                                    self.valid_moves(self.current_player+1)
                                else:
                                    self.still_playing = False

    def valid_moves(self,player):                                                   # Checking for valid moves for a player
        if player == 1:
            opponent = 2
        else: 
            opponent = 1
        self.board = np.where(self.board == 3 , 0 , self.board)
        for j in range(self.size):
            for i in range(self.size):
                if self.board[i][j] == 0:
                    for dx,dy in self.directions:
                        x=i+dx
                        y=j+dy
                        found = False
                        while 0 <=x < self.size and 0<= y < self.size:
                            if self.board[x][y] == opponent:
                                found = True
                            elif self.board[x][y] == player and found:
                                self.board[i][j] = 3
                                break
                            else:
                                break
                            x+=dx
                            y+=dy

    def check_playing(self):                                                        # checking for further possibilty of game
        self.valid_moves(1)
        if np.any(self.board == 3):
            return True
        self.valid_moves(2)
        if np.any(self.board == 3):
            return True
        
        self.game_over_time = pygame.time.get_ticks()                               # storing game end time 
        return False
    
    def check_win(self):                                                            # Finding winner after game play
        if self.player_count(1) > self.player_count(2):
            return 1
        elif self.player_count(1) < self.player_count(2):
            return 2
        else:
            return 1,2

    def update_board(self,i,j):                                                     # Updating board and flipping relevant discs
        if self.current_player == 0:
            opponent = 2
        else:
            opponent = 1
        self.board = np.where(self.board == 3 , 0 , self.board)
        self.board[i][j] = self.current_player + 1
        for dx,dy in self.directions:
            x=i+dx
            y=j+dy
            found = False
            to_flip = []
            while 0 <=x < self.size and 0<= y < self.size:
                if self.board[x][y] == opponent:
                    found = True
                    if 0 <=x+dx < self.size and 0<=y+dy<self.size:
                        to_flip.append((x,y))
                    else:
                        to_flip = []
                elif self.board[x][y] == self.current_player + 1 and found:
                    break
                else:
                    to_flip = []
                    break
                x+=dx
                y+=dy
            for x,y in to_flip:
                self.board[x][y] = self.current_player + 1



    def display_board(self):                                                        # Displaying Board with marked discs
        pygame.draw.rect(self.surface,(46,140,87),(350,100,800,800),0,15)
        pygame.draw.rect(self.surface,(58,36,22),(350,100,800,800),10,15)
        for i in range(self.size):
            for j in range(self.size):
                pygame.draw.rect(self.surface,(0,0,0),(350+j*100,100+100*i,100,100),2)
                if self.board[i][j] == 1:
                    pygame.draw.circle(self.surface,(0,0,0),(400+j*100,150+100*i),40)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(self.surface,(255,255,255),(400+j*100,150+100*i),40)
                elif self.board[i][j] == 3:
                    if self.current_player == 0:
                        pygame.draw.circle(self.surface,(0,0,0),(400+j*100,150+100*i),40,2)
                    else:
                        pygame.draw.circle(self.surface,(255,255,255),(400+j*100,150+100*i),40,2)


    def play(self):

        # Player Scores Displaying
        Black_score = self.font.render(f"Black : {self.player_count(1)}",1,(255,255,255))
        White_score = self.font.render(f"White : {self.player_count(2)}",1,(255,255,255))
        pygame.draw.circle(self.surface,(0,0,0),(75,450),30)
        self.surface.blit(Black_score,(120,437))
        pygame.draw.circle(self.surface,(255,255,255),(75,550),30)
        self.surface.blit(White_score,(120,537))

        # While playing 
        if self.still_playing:
            if (np.any(self.board == 3)):
                self.display_board()
            else:
                self.display_board()
                Text = self.font.render(f"There are no Valid moves for Player{self.current_player + 1}",1,(255,255,255))
                Text_rect = Text.get_rect()
                Text_rect.center = (self.surface.get_rect().centerx,500)
                pygame.draw.rect(self.surface,(0,0,0),(300,400,900,300),0,15)
                self.surface.blit(Text,Text_rect)
                pygame.draw.rect(self.surface,(0,200,0),self.ok_button["button_pos"],0,15)
                self.surface.blit(self.ok_button["text"],self.ok_button["text_pos"])
        # After no valid moves
        else:
            self.display_board()
            pygame.draw.rect(self.surface,(0,0,0),(300,400,900,300),0,15)
            Text_1 = self.font.render(f"No more valid moves",1,(255,255,255))
            Text_1_rect = Text_1.get_rect()
            Text_1_rect.center = (750,500)
            winner = self.check_win()
            if winner == 1 or winner == 2:
                if winner == 1:
                    player = "Black"
                else:
                    player = "White"
                Text_2 = self.font.render(f"{player} won with a majority of {self.player_count(winner)-self.player_count(3-winner)}",1,(255,255,255))
            else:
                Text_2 = self.font.render(f"Game is Draw",1,(255,255,255))
            Text_2_rect =Text_2.get_rect()
            Text_2_rect.center = (self.surface.get_rect().centerx,550)

            # Redirecting Text
            redirecting_text = self.font.render(f"Redirecting in... {int(4 - int(pygame.time.get_ticks()-self.game_over_time)/1000)}'s",1,(255,255,255))
            redirecting_text_rect = redirecting_text.get_rect()
            redirecting_text_rect.center = (self.surface.get_rect().centerx,650)

            # Displaying texts on to the screen
            self.surface.blit(Text_1,Text_1_rect)
            self.surface.blit(Text_2,Text_2_rect)
            self.surface.blit(redirecting_text,redirecting_text_rect)

            # Appending into history.csv
            if pygame.time.get_ticks() - self.game_over_time >= 3000:
                if winner == 1 or winner == 2:
                    self.results={
                        "winner":self.players[winner-1],
                        "loser": self.players[2-winner],
                        "date-time":datetime.now().ctime(),
                        "game":"othello"
                    }
                else:
                    self.results={
                        "date-time":datetime.now().ctime(),
                        "game":"othello"
                    }
                    

