from base_game import Game,mouse_pos,load_img
import os
import pygame
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# Creating connect4 class using inheritance
class connect4(Game):

    def __init__(self,players,current_player,surface,size):             # Using same init as in Game class
        self.still_playing = True
        super().__init__(players,current_player,surface,size)

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