# ***Mini Game Hub***
# ***Harshitha - Poorna Sai***

A two player game hub constructed using **Bash**,**Python** and **Pygame**. Authentication and Analytics part is done using **Bash**, and the Gaming part is done using **Python** and **Pygame**. Games are played in a seperate Graphical Interface using **Pygame GUI**.

___

# Directory Structure 

```
mini-game-hub/
├── main.sh
├── game.py
├── base_game.py
├── leaderboard.sh
├── requirements.txt
├── .gitattributes
├── games/
│   ├── tictactoe.py
│   ├── othello.py
│   └── connect4.py
├── assets/
│   ├── background_images/
│       ├── connect4_bg.png
│       ├── tictactoe_bg.png
│       ├── menu_bg1.png
│       ├── menu_bg2.png
│       ├── othello_bg.png
│   ├── fonts/
│       ├── Celinda.ttf
│       ├── Retro.ttf
│
├── users.tsv
├── history.csv
└── README.md
```

____

# Features Implemented in User Authentication

- Prompt for Login 
- Added an option ("Enter '#'" in login form) to open Signup form
- Error Handling for Username and Password
- Hashing the Password before storing in users.tsv
- Ensuring both players are different
- Added Colours for Error and Success messages

# Features Implemented in Game Play

- Interactive buttons and hover effects
- Back and Quit buttons for easy navigation
- Displaying Player turns while playing game
- Implemented Draw Condition 
- Waiting for 3 seconds after game completion to display options for displaying statistics, Play again and Quit
- User has choice to select preference of sorting
- Dynamic preview effects are shown in connect4 and valid moves 

# Features Implemented in Leaderboard and Matplotlib charts

- Leaderboard will be displayed based on the selection of users
- 3 graphs related statistics will be displayed after clicking matlplotlib 

____

# How to Run

``` bash main.sh```

____

# How to install python modules

Run the following command:
``` pip install -r requirments.txt ```

---

# How to Run Through the Game 

Use interactive buttons to navigate through pages, Click on the board to update board accordingly and if a player have no more valid moves in othello a prompt will be appeared saying "No more valid moves for the respective player". After completion of game you should wait for 3 sec and after that you will be redirected to last page having option's to see matplotlib, leaderboard, play again and quit.

If users enter quit the game will be closed smoothly

---

# Future Implementations
If there was more time given following implimentations may be done

- Reset Password functionalit in User Authentication
- More matplotlib charts
- Background Music 
- Instructions Page