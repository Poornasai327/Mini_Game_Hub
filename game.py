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

def load_img(filename,scale):                                           # For loading images and scaling
    img = pygame.image.load(filename).convert_alpha()
    if img.get_size() != scale:
        return pygame.transform.scale(img,scale)
    else:
        return img
    
def create_button(Text,color,font,centerx,centery,height,width):        # For creating buttons 
    rect = pygame.rect.Rect(0,0,width,height)
    rect.center = (centerx,centery)
    text = font.render(Text,1,color)
    pos = text.get_rect()
    pos.center = (centerx,centery)
    return {"text":text,"text_pos":pos,"button_pos":rect}                # Returns a dictionary with text, text position and button rect positons

def hover(button,speedx,speedy):                                # To create hover effect
    if button["button_pos"].collidepoint(mouse_pos()):
        if button["button_pos"].height < 90:
            button["button_pos"].height += speedy
        if button["button_pos"].width < 310:
            button["button_pos"].width += speedx
    else:
        if button["button_pos"].height > 80:
            button["button_pos"].height -= speedy
        if button["button_pos"].width > 300:
            button["button_pos"].width -= speedx
    button["button_pos"].center = button["text_pos"].center       
    return

def main():
    players = [sys.argv[1],sys.argv[2]]
    pygame.init()
    screen = pygame.display.set_mode((1500,1000))                    # Creating GUI window
    caption = pygame.display.set_caption("Mini Game Hub")

    # Creating a Menu Surface for smooth handling
    Menu_Surface = pygame.Surface(screen.get_size())

    # Loading Background Images
    Menu_bg1 = load_img(os.path.join(os.path.join('background_images','Mini game hub celebration scene.png')),Menu_Surface.get_size())
    Menu_bg2 = load_img(os.path.join('background_images','Arcade game selection mini-room.png'),Menu_Surface.get_size())

    # Defining font styles
    font = pygame.font.Font(None,52)

    # Creating buttons
    Select_button = create_button("Select Game",(255,255,255),font,Menu_Surface.get_rect().centerx,380,80,300)
    Instructions_button = create_button("Instructions",(255,255,255),font,Menu_Surface.get_rect().centerx,540,80,300)
    Quit_button = create_button("Quit",(255,255,255),font,Menu_Surface.get_rect().centerx,700,80,300)
    Tic_button = create_button("Tic Tac Toe",(255,255,255),font,Menu_Surface.get_rect().centerx,300,80,300)
    Connect4_button = create_button("Connect4",(255,255,255),font,Menu_Surface.get_rect().centerx,460,80,300)
    Othello_button = create_button("Othello",(255,255,255),font,Menu_Surface.get_rect().centerx,620,80,300)
    Back_button = create_button("Back",(255,255,255),font,200,100,80,300)

    # For running GUI window
    Menu = True
    Menu_State = 1
    while Menu:

        if Menu_State == 1:
            Menu_Surface.blit(Menu_bg1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                           # For closing GUI window
                    Menu = False
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((1500,1000))
                hover(Select_button,1,2)
                hover(Instructions_button,1,2)
                hover(Quit_button,1,2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Select_button["button_pos"].collidepoint(mouse_pos()):
                        Menu_State = 2
                        Select_button["button_pos"].height = 80                   # Keeping the button into original state.
                        Select_button["button_pos"].width = 300
                        Select_button["button_pos"].center = Select_button["text_pos"].center
                    if Quit_button["button_pos"].collidepoint(mouse_pos()):
                        Menu = False

            # Drawing rects and blitting buttons
            pygame.draw.rect(Menu_Surface,(0, 200, 0),Select_button["button_pos"],0,15)
            pygame.draw.rect(Menu_Surface,(0, 200, 0),Instructions_button["button_pos"],0,15)
            pygame.draw.rect(Menu_Surface,(0, 200, 0),Quit_button["button_pos"],0,15)
            Menu_Surface.blit(Select_button["text"],Select_button["text_pos"])
            Menu_Surface.blit(Instructions_button["text"],Instructions_button["text_pos"])
            Menu_Surface.blit(Quit_button["text"],Quit_button["text_pos"])
        
        if Menu_State == 2:
            Menu_Surface.blit(Menu_bg2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu = False
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((1500,1000))
                hover(Tic_button,1,2)
                hover(Connect4_button,1,2)
                hover(Othello_button,1,2)
                hover(Back_button,1,2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_button["button_pos"].collidepoint(mouse_pos()):
                        Menu_State = 1
                        Back_button["button_pos"].height = 80                               # Keeping the button into original state.
                        Back_button["button_pos"].width = 300
                        Back_button["button_pos"].center = Back_button["text_pos"].center

            # Drawing rects and blitting buttons
            pygame.draw.rect(Menu_Surface,(0, 200, 0),Tic_button["button_pos"],0,15)
            pygame.draw.rect(Menu_Surface,(0, 200, 0),Connect4_button["button_pos"],0,15)
            pygame.draw.rect(Menu_Surface,(0, 200, 0),Othello_button["button_pos"],0,15)
            pygame.draw.rect(Menu_Surface,(200,0,0),Back_button["button_pos"],0,15)
            Menu_Surface.blit(Back_button["text"],Back_button["text_pos"])
            Menu_Surface.blit(Connect4_button["text"],Connect4_button["text_pos"])
            Menu_Surface.blit(Othello_button["text"],Othello_button["text_pos"])
            Menu_Surface.blit(Tic_button["text"],Tic_button["text_pos"])

        # Blitting everuthing on to the screen   
        screen.blit(Menu_Surface)
        pygame.display.flip()


if __name__ == "__main__":
    main()