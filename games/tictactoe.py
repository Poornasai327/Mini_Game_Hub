from base_game import Game,mouse_pos,load_img
import os
import pygame
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# Creating tictactoe class using inheritance
class tictactoe(Game):

    def __init__(self,players,current_player,surface,size):          # Using same init as in Game class
        self.still_playing=True
        return super().__init__(players,current_player,surface,size)

    def check_win(self):                                        
        window_board = sliding_window_view(self.board,(5,5))            # Converting board into 5*5 small boards
        if np.any(np.all(window_board == self.current_player + 1 , axis= -2)):      # Checking along vertical columns
            return True
        elif np.any(np.all(window_board == self.current_player + 1 ,axis = -1)):    # Checking along horizontal rows
            return True
        # Checking along diagonals
        elif np.any(np.all(np.diagonal(np.flip(window_board,axis=-1),axis1=-1,axis2=-2) == self.current_player + 1, axis=-1)):
            return True
        elif np.any(np.all(np.diagonal(window_board,axis1=-1,axis2=-2) == self.current_player + 1,axis=-1)):
            return True
        else:
            return False

    def change_turn(self):                                  # Using same change_turn method as in Game class
        return super().change_turn()
    
    def update_board(self,i,j):                             # Updating numpy board according to position of click
        self.board[i][j] = self.current_player + 1

    def display_board(self):
        pygame.draw.rect(self.surface,(28,28,45),(350,100,800,800),0,0)     # Drawing background for game board

        for i in range(self.size):                                          # Displaying X and O's
            for j in range(self.size):
                pygame.draw.rect(self.surface,(130,80,255),(350+80*j,100+80*i,80,80),2)

                if self.board[i][j] == 1:
                    pygame.draw.circle(self.surface,(0,255,170),(390+80*j,140+80*i),32,4)
                elif self.board[i][j] == 2:
                    pygame.draw.line(self.surface,(255,30,120),(360+80*j,110+80*i),(420+80*j,170+80*i),4)
                    pygame.draw.line(self.surface,(255,30,120),(360+80*j,170+80*i),(420+80*j,110+80*i),4)

    def handle_click(self,mx,my):                           # Handling mouse click and updating the board accordingly
        if self.still_playing:
            for j in range(self.size):
                if 350 + 80*j < mx < 430 + 80*j:
                    for i in range(self.size):
                        if 100 + 80*i < my < 180 + 80*i:
                            if self.board[i][j] == 0:
                                self.update_board(i,j)
                                if self.check_win():               # Checking win condition after a click
                                    self.still_playing=False       # Ending the game
                                else:
                                    self.change_turn()

    def play(self):
        self.display_board()