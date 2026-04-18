import numpy as np
import sys
import pygame
import os
from base_game import mouse_pos,load_img,create_button,hover,reset_button
from games.connect4 import connect4

def main():
    players = [sys.argv[1],sys.argv[2]]
    pygame.init()
    screen = pygame.display.set_mode((1500,1000))                    # Creating GUI window
    caption = pygame.display.set_caption("Mini Game Hub")

    # Creating a Menu Surface for smooth handling
    Game_Surface = pygame.Surface(screen.get_size())

    # Loading Background Images
    Menu_bg1 = load_img(os.path.join(os.path.join('background_images','Mini game hub celebration scene.png')),Game_Surface.get_size())
    Menu_bg2 = load_img(os.path.join('background_images','Arcade game selection mini-room.png'),Game_Surface.get_size())
    connect4_bg = load_img(os.path.join("background_images","dark-hexagonal-background-with-gradient-color_79603-1409.png"),Game_Surface.get_size())

    # Defining font styles
    font = pygame.font.Font(None,52)

    # Creating buttons
    Select_button = create_button("Select Game",(255,255,255),font,Game_Surface.get_rect().centerx,380,80,300)
    Instructions_button = create_button("Instructions",(255,255,255),font,Game_Surface.get_rect().centerx,540,80,300)
    Quit_button = create_button("Quit",(255,255,255),font,Game_Surface.get_rect().centerx,700,80,300)
    Tic_button = create_button("Tic Tac Toe",(255,255,255),font,Game_Surface.get_rect().centerx,300,80,300)
    Connect4_button = create_button("Connect4",(255,255,255),font,Game_Surface.get_rect().centerx,460,80,300)
    Othello_button = create_button("Othello",(255,255,255),font,Game_Surface.get_rect().centerx,620,80,300)
    Back_button = create_button("Back",(255,255,255),font,150,80,80,200)

    # Creating and Initialising Game Objects
    connect4_game = connect4(players,0,Game_Surface,7)

    # For running GUI window
    Playing = True
    Game_State = 1
    while Playing:

        if Game_State == 1:
            Game_Surface.blit(Menu_bg1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                           # For closing GUI window
                    Playing = False
                if event.type == pygame.VIDEORESIZE:                    # For not allowwing resizing in linux
                    screen = pygame.display.set_mode((1500,1000))
                hover(Select_button,1,2,80,300)                         # To create hover effect
                hover(Instructions_button,1,2,80,300)
                hover(Quit_button,1,2,80,300)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Select_button["button_pos"].collidepoint(mouse_pos()):
                        Game_State = 2
                        reset_button(Select_button,80,300)
                    if Quit_button["button_pos"].collidepoint(mouse_pos()):
                        Playing = False

            # Drawing rects and blitting buttons
            pygame.draw.rect(Game_Surface,(139, 92, 246),Select_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(168, 85, 247),Instructions_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(239, 68, 68),Quit_button["button_pos"],0,15)
            Game_Surface.blit(Select_button["text"],Select_button["text_pos"])
            Game_Surface.blit(Instructions_button["text"],Instructions_button["text_pos"])
            Game_Surface.blit(Quit_button["text"],Quit_button["text_pos"])
        
        if Game_State == 2:
            Game_Surface.blit(Menu_bg2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Playing = False
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((1500,1000))
                hover(Tic_button,1,2,80,300)
                hover(Connect4_button,1,2,80,300)
                hover(Othello_button,1,2,80,300)
                hover(Back_button,1,2,80,200)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_button["button_pos"].collidepoint(mouse_pos()):
                        Game_State = 1
                        reset_button(Back_button,80,200)
                    if Connect4_button["button_pos"].collidepoint(mouse_pos()):
                        Game_State = 3
                        game = "connect4"
                        reset_button(Connect4_button,80,300)

            # Drawing rects and blitting buttons
            pygame.draw.rect(Game_Surface,(79, 70, 229),Tic_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(79, 70, 229),Connect4_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(79, 70, 229),Othello_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(220, 38, 38),Back_button["button_pos"],0,15)
            Game_Surface.blit(Back_button["text"],Back_button["text_pos"])
            Game_Surface.blit(Connect4_button["text"],Connect4_button["text_pos"])
            Game_Surface.blit(Othello_button["text"],Othello_button["text_pos"])
            Game_Surface.blit(Tic_button["text"],Tic_button["text_pos"])

        if Game_State == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Playing = False
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((1500,1000))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = mouse_pos()
                    if Back_button["button_pos"].collidepoint((mx,my)):
                        Game_State = 2
                        reset_button(Back_button,80,200)
                        connect4_game = connect4(players,0,Game_Surface,7)
                    if game == "connect4":
                        connect4_game.handle_click(mx,my)                               # To update game board in connect4
                hover(Back_button,1,2,80,200)
            if game == "connect4":
                Game_Surface.blit(connect4_bg)
                connect4_game.play()

            pygame.draw.rect(Game_Surface,(220, 38, 38),Back_button["button_pos"],0,15)
            Game_Surface.blit(Back_button["text"],Back_button["text_pos"])
        # Blitting everuthing on to the screen   
        screen.blit(Game_Surface)
        pygame.display.flip()


if __name__ == "__main__":
    main()