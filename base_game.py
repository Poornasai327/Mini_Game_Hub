import pygame
import numpy as np
import sys
import matplotlib.pyplot as plt
import csv


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

def append_history(results):                                            # Appending history with relevant draw case
    if "winner" in results.keys():
        with open("history.csv","a") as f:
            f.write(f'{results["winner"]},{results["loser"]},{results["date-time"]},{results["game"]},no\n')
    else:
        with open("history.csv","a") as f:
            f.write(f'{sys.argv[1]},{sys.argv[2]},{results["date-time"]},{results["game"]},yes\n')

def matplotlib_charts():
    wins={}
    losses={}
    games={}

    with open("history.csv","r") as file:                       # Reading history.csv
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            winner = line[0]
            loser = line [1]
            game = line[3]

            if winner in wins:
                wins[winner] += 1
            else:
                wins[winner] = 1
                
            if loser in losses:
                losses[loser] += 1
            else:
                losses[loser] = 1

            if game in games:
                games[game] += 1
            else:
                games[game] = 1

    font1 = {'family': 'serif', 'color': '#1f3b73', 'size': 20, 'weight': 'bold'}
    font2 = {'family': 'sans-serif', 'color': '#333333', 'size': 13 }

    # 1. Top 5 players sorted wins (Bar Graph)
    def get_wins(item):
        return item[1]
        
    top5 = sorted(wins.items(), key=get_wins, reverse=True)[:5]
    players = [x[0] for x in top5]
    win_counts = [x[1] for x in top5]

    plt.figure()
    plt.bar(players, win_counts, color='lightblue')
    plt.title("Top 5 Players sorted by Wins", fontdict=font1)
    plt.xlabel("Players", fontdict=font2)
    plt.ylabel("Wins", fontdict=font2)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # 2. Frequency of games played ( Pie Chart)
    plt.figure()
    plt.pie(games.values(), labels=games.keys(), autopct='%1.2f%%')
    plt.title("Frequency of Games played", fontdict=font1)
    plt.tight_layout()
    plt.show()

    # 3. Top 7 players wins vs losses (Bar Graph)
    top7 = sorted(wins.items(), key=get_wins, reverse=True)[:7]
    players = [x[0] for x in top7]
    win_counts = [x[1] for x in top7]
    loss_counts = [losses.get(player, 0) for player in players]
    x = np.arange(len(players))

    plt.figure()
    plt.bar(x-0.2, win_counts, 0.4, label="Wins")
    plt.bar(x+0.2, loss_counts, 0.4, label="Losses")
    plt.xticks(x, players)
    plt.title("Wins vs Losses (Top 7 Players)", fontdict=font1)
    plt.xlabel("Players", fontdict=font2)
    plt.ylabel("Count", fontdict=font2)
    plt.grid(axis='y')
    plt.legend()
    plt.show()