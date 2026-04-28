import numpy as np
import sys
import pygame
import os
from base_game import mouse_pos,load_img,create_button,hover,reset_button,append_history
from games.connect4 import connect4
from games.tictactoe import tictactoe
from games.othello import othello

def main():

    if not os.path.exists("history.csv"):                           # Creating history.csv file if not present
        with open("history.csv","w") as f:
            f.write(f"winner,loser,date-time,game,isdraw\n")

    players = [sys.argv[1],sys.argv[2]]
    pygame.init()

    # screen details
    screen_size = (1500,1000)
    screen = pygame.display.set_mode(screen_size)                    # Creating GUI window
    caption = pygame.display.set_caption("Mini Game Hub")

    # Creating a Menu Surface for smooth handling
    Game_Surface = pygame.Surface(screen_size)
    Game_Surface_centerx = Game_Surface.get_rect().centerx
    Game_Surface_centery = Game_Surface.get_rect().centery

    # Loading Background Images
    Menu_bg1 = load_img(os.path.join(os.path.join('background_images','menu_bg1.png')),screen_size)
    Menu_bg2 = load_img(os.path.join('background_images','menu_bg2.png'),screen_size)
    connect4_bg = load_img(os.path.join("background_images","connect4_bg.png"),screen_size)
    tictactoe_bg = load_img(os.path.join("background_images","tictactoe_bg.png"),screen_size)
    othello_bg = load_img(os.path.join("background_images","othello_bg.png"),screen_size)

    # Defining font styles
    font = pygame.font.Font(None,52)

    # Creating buttons
    Select_button = create_button("Select Game",(255,255,255),font,Game_Surface_centerx,380,80,300)
    Instructions_button = create_button("Instructions",(255,255,255),font,Game_Surface_centerx,540,80,300)
    Quit_button = create_button("Quit",(255,255,255),font,Game_Surface_centerx,700,80,300)
    Tic_button = create_button("Tic Tac Toe",(255,255,255),font,Game_Surface_centerx,300,80,300)
    Connect4_button = create_button("Connect4",(255,255,255),font,Game_Surface_centerx,460,80,300)
    Othello_button = create_button("Othello",(255,255,255),font,Game_Surface_centerx,620,80,300)
    Back_button = create_button("Back",(255,255,255),font,150,80,80,200)
    Play_again_button = create_button("Play Again",(255,255,255),font,Game_Surface_centerx,380,80,300)
    Display_leaderboard_button = create_button("Leaderboard",(255,255,255),font,Game_Surface_centerx,540,80,300)
    Show_charts_button = create_button("Matplotlib",(255,255,255),font,Game_Surface_centerx,700,80,300)

    # Creating and Initialising Game Objects
    connect4_game = connect4(players,0,Game_Surface,7)
    tictactoe_game = tictactoe(players,0,Game_Surface,10)
    othello_game = othello(players,0,Game_Surface,8)

    # Results dictionary
    results = {}

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
                    mx,my = mouse_pos()
                    if Back_button["button_pos"].collidepoint((mx,my)):
                        Game_State = 1
                        reset_button(Back_button,80,200)
                    if Connect4_button["button_pos"].collidepoint((mx,my)):
                        Game_State = 3
                        game = "connect4"
                        reset_button(Connect4_button,80,300)
                    if Tic_button["button_pos"].collidepoint((mx,my)):
                        Game_State = 3
                        game = "tictactoe"
                        reset_button(Tic_button,80,300)
                    if Othello_button["button_pos"].collidepoint((mx,my)):
                        Game_State = 3
                        game = "othello"
                        reset_button(Othello_button,80,300)

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
                        # resetting game states after clicking back button while playing
                        connect4_game = connect4(players,0,Game_Surface,7)
                        tictactoe_game = tictactoe(players,0,Game_Surface,10)
                        othello_game = othello(players,0,Game_Surface,8)
                    if game == "connect4":
                        connect4_game.handle_click(mx,my)                               # To update game board in connect4
                    elif game == "tictactoe":
                        tictactoe_game.handle_click(mx,my)                              # To update game board in tictactoe
                    elif game == "othello":
                        othello_game.handle_click(mx,my)                                # To update game board in othello
                hover(Back_button,1,2,80,200)
                hover(othello_game.ok_button,1,2,80,300)

            # while playing games
            if game == "connect4":
                Game_Surface.blit(connect4_bg)
                connect4_game.play()
                results = connect4_game.results
            elif game == "tictactoe":
                Game_Surface.blit(tictactoe_bg)
                tictactoe_game.play()
                results = tictactoe_game.results
            elif game == "othello":
                Game_Surface.blit(othello_bg)
                othello_game.play()
                results = othello_game.results

            # Appending results into history.csv and resetting game states
            if len(results) > 0:
                append_history(results)
                Game_State = 4
                connect4_game = connect4(players,0,Game_Surface,7)
                tictactoe_game = tictactoe(players,0,Game_Surface,10)
                othello_game = othello(players,0,Game_Surface,8)

            pygame.draw.rect(Game_Surface,(220, 38, 38),Back_button["button_pos"],0,15)
            Game_Surface.blit(Back_button["text"],Back_button["text_pos"])

        if Game_State == 4:
            Game_Surface.blit(Menu_bg1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = mouse_pos()
                    if Play_again_button["button_pos"].collidepoint((mx,my)):
                        Game_State = 1
                        reset_button(Play_again_button,80,300)
                    if Display_leaderboard_button["button_pos"].collidepoint((mx,my)):
                        pass
                    if Show_charts_button["button_pos"].collidepoint((mx,my)):
                        pass
                hover(Play_again_button,1,2,80,300)
                hover(Display_leaderboard_button,1,2,80,300)
                hover(Show_charts_button,1,2,80,300)

            pygame.draw.rect(Game_Surface,(139, 92, 246),Play_again_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(168, 85, 247),Display_leaderboard_button["button_pos"],0,15)
            pygame.draw.rect(Game_Surface,(139, 92, 246),Show_charts_button["button_pos"],0,15)
            Game_Surface.blit(Play_again_button["text"],Play_again_button["text_pos"])
            Game_Surface.blit(Display_leaderboard_button["text"],Display_leaderboard_button["text_pos"])
            Game_Surface.blit(Show_charts_button["text"],Show_charts_button["text_pos"])
        # Blitting everuthing on to the screen   
        screen.blit(Game_Surface)
        pygame.display.flip()


if __name__ == "__main__":
    main()