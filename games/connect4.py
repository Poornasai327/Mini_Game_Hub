from base_game import Game,mouse_pos,load_img
from datetime import datetime
import pygame
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# Creating connect4 class using inheritance
class connect4(Game):

    def __init__(self,players,current_player,surface,size):             # Using same init as in Game class
        self.still_playing = True
        self.font = pygame.font.Font(None,52)
        super().__init__(players,current_player,surface,size)
        self.results = {}

    def check_win(self):
        window_board = sliding_window_view(self.board,(4,4))
        if np.any(np.all(window_board == self.current_player + 1 ,axis = -2)):          # Checking Verical line
            return True
        elif np.any(np.all(window_board == self.current_player + 1 ,axis = -1)):        # Checking horizontal line
            return True
        # Checking Diagonals
        elif np.any(np.all(np.diagonal(np.flip(window_board,axis=-1),axis1=-1,axis2=-2) == self.current_player + 1, axis=-1)):
            return True
        elif np.any(np.all(np.diagonal(window_board,axis1=-1,axis2=-2) == self.current_player + 1,axis=-1)):
            return True
        else:
            return False
        
    def check_draw(self):                                                               # Checking Draw case
        if 0 not in self.board:
            self.still_playing = False

    def change_turn(self):                                              # Using same change_turn method as in Game class
        return super().change_turn()
    
    def update_board(self,i,j):                                         # Updating numpy board according to position of click
        self.board[i][j] = self.current_player + 1

    def display_board(self):
        pygame.draw.rect(self.surface,(58, 80, 107),(350,100,800,800),0,20)         # Drawing background for game board
        for i in range(self.size):                                                  # Displaying marked cells and empty cells with different colors
            for j in range(self.size):
                if self.board[i][j] == 1:
                    pygame.draw.circle(self.surface,(39, 180, 151),(420+110*j,170+110*i),40)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(self.surface,(232, 93, 117),(420+110*j,170+110*i),40)
                else:
                    pygame.draw.circle(self.surface,(11, 30, 45),(420+110*j,170+110*i),40)

    def handle_click(self,mx,my):                                                # Handling mouse click and updating the board accordingly
        if self.still_playing:
            for j in range(self.size):
                if 380+110*j < mx < 460+110*j:
                    for i in range(self.size-1,-1,-1):
                        if self.board[i][j] == 0:
                            self.update_board(i,j)
                            if self.check_win():
                                self.still_playing = False
                                self.game_over_time = pygame.time.get_ticks()
                            elif self.check_draw():
                                self.still_playing = False
                                self.game_over_time = pygame.time.get_ticks()
                            else:
                                self.change_turn()
                            break

    def show_preview(self):                                                         # Creating hover effect over cells in display using mouse position
        for j in range(self.size):
            if mouse_pos()[0] > 380+110*j and mouse_pos()[0] < 460+110*j:
                    for i in range(self.size-1,-1,-1):
                        if self.board[i][j] == 0:
                            if self.current_player == 0:
                                pygame.draw.circle(self.surface,(44, 140, 125),(420+110*j,170+110*i),40)
                            else:
                                pygame.draw.circle(self.surface,(242, 138, 155),(420+110*j,170+110*i),40)
                            break

    def play(self):

        self.display_board()
        if self.still_playing:      # Displaying preview effect if still playing
            self.show_preview()

            # Displaying players turns
            if self.current_player == 0:
                Text = self.font.render("Green's Turn",1,(255,255,255))
            else:
                Text = self.font.render("Red's Turn",1,(255,255,255))
            Text_rect = Text.get_rect()
            Text_rect.center = (750,50)
            self.surface.blit(Text,Text_rect)

        else:
            # Showing redirection text
            redirecting = self.font.render(f"Redirecting in... {int(4-int(pygame.time.get_ticks()-self.game_over_time)/1000)}'s",1,(255,255,255))
            redirecting_rect = redirecting.get_rect()
            redirecting_rect.center = (self.surface.get_rect().centerx,950)
            self.surface.blit(redirecting,redirecting_rect)

            # Displaying who is winner
            if self.check_win():
                if self.current_player == 0:
                    winner_text = self.font.render("Green Won",1,(255,255,255))
                else:
                    winner_text = self.font.render("Red Won",1,(255,255,255))
                winner_text_rect = winner_text.get_rect()
                winner_text_rect.center = (self.surface.get_rect().centerx,50)
                self.surface.blit(winner_text,winner_text_rect)
            elif self.check_draw():
                draw_text = self.font.render("Game is Draw",1,(255,255,255))
                draw_text_rect = draw_text.get_rect()
                draw_text_rect.center = (self.surface.get_rect().centerx,50)
                self.surface.blit(draw_text,draw_text_rect)

            # Appending results after 3 seconds
            if pygame.time.get_ticks() - self.game_over_time >= 3000:
                if self.check_win():
                    self.results = {
                    "winner":self.players[self.current_player],
                    "loser":self.players[(self.current_player+1)%2],
                    "date-time":datetime.now().ctime(),
                    "game":"connect4"
                    }
                elif self.check_draw():
                    self.results = {
                        "date-time":datetime.now().ctime(),
                        "game":"connect4"
                    }