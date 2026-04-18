import pygame
import numpy as np

class Game:

    def __init__(self,players,current_player,surface,size):                     # Initialising Game object    
        self.players = players
        self.board = np.full((size,size),0)
        self.current_player = current_player
        self.surface = surface
        self.size = size

    def change_turn(self):
        self.current_player = (self.current_player + 1)%2                     # Way to Change turns

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

def hover(button,speedx,speedy,height,width):                                # To create hover effect
    if button["button_pos"].collidepoint(mouse_pos()):
        if button["button_pos"].height < height+10:
            button["button_pos"].height += speedy
        if button["button_pos"].width < width+10:
            button["button_pos"].width += speedx
    else:
        if button["button_pos"].height > height:
            button["button_pos"].height -= speedy
        if button["button_pos"].width > width:
            button["button_pos"].width -= speedx
    button["button_pos"].center = button["text_pos"].center       
    return

def reset_button(button,height,width):                                   # Keeping the button into original state.
    button["button_pos"].height = height
    button["button_pos"].width = width
    button["button_pos"].center = button["text_pos"].center