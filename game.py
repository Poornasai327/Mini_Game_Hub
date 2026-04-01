import numpy as np
import sys
import pygame
import os

class Game:

    def __init__(self,players,playing,size):                    
        self.players = players
        self.board = np.full((size,size),"-")
        self.playing = playing

    def change_turn(self):
        self.playing = (self.playing + 1)%2                     # Way to Change turns

    def check_win(self):
        pass                # Each game has its own win conditions

def mouse_pos():
    return pygame.mouse.get_pos()

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))                    # Creating GUI window
    caption = pygame.display.set_caption("Mini Game Hub")
    Menu = True

    while Menu:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                           # For closing GUI window
                Menu = False
        pygame.display.flip()


if __name__ == "__main__":
    main()