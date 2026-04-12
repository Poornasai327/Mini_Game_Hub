from base_game import Game,mouse_pos,load_img
import os
import pygame
import numpy

class connect4(Game):

    def __init__(self,players,current_player,surface,size):
        super().__init__(players,current_player,surface,size)

    def check_win(self):
        pass

    def change_turn(self):
        return super().change_turn()
    
    def update_board(self,i,j):
        self.board[i][j] = self.current_player + 1

    def play(self):
        connect4_bg = load_img(os.path.join("background_images","dark-hexagonal-background-with-gradient-color_79603-1409.png"),self.surface.get_size())
        self.surface.blit(connect4_bg)
        pygame.draw.rect(self.surface,(58, 80, 107),(350,100,800,800),0,20)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    pygame.draw.circle(self.surface,(39, 180, 151),(420+110*j,170+110*i),40)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(self.surface,(232, 93, 117),(420+110*j,170+110*i),40)
                else:
                    pygame.draw.circle(self.surface,(11, 30, 45),(420+110*j,170+110*i),40)
        
        for j in range(self.size):
            if mouse_pos()[0] > 380+110*j and mouse_pos()[0] < 460+110*j:
                    for i in range(self.size-1,-1,-1):
                        if self.board[i][j] == 0:
                            if self.current_player == 0:
                                pygame.draw.circle(self.surface,(44, 140, 125),(420+110*j,170+110*i),40)
                            else:
                                pygame.draw.circle(self.surface,(242, 138, 155),(420+110*j,170+110*i),40)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    self.update_board(i,j)
                                    self.change_turn()
                            break