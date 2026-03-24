# ***Mini Game Hub***

A two player game hub constructed using **Bash**,**Python** and **Pygame**. Authentication and Analytics part is done using **Bash**, and the Gaming part is done using **Python** and **Pygame**. Games are played in a seperate Graphical Interface using **Pygame GUI**.

___

# Directory Structure 

```
mini-game-hub/
├── main.sh
├── game.py
├── leaderboard.sh
├── requirements.txt
│
├── games/
│   ├── tictactoe/
│   │   ├── tictactoe.py
│   │   ├── background.png
│   │   └── background.mp3
│   │
│   ├── othello/
│   │   ├── othello.py
│   │   ├── background.png
│   │   └── background.mp3
│   │
│   └── connect4/
│       ├── connect4.py
│       ├── background.png
│       └── background.mp3
│
├── users.tsv
├── history.csv
└── README.md
```

____

# Features Planned in main.sh 

- Prompt for Login 
- Added an option ("Enter '#'" in login form) to open Signup form
- Error Handling for Username and Password
- Hashing the Password before storing in users.tsv
- Ensuring both players are different
- Providing forget password option to end Users
- Added Colours for Error and Success messages

____

# How to Run

``` bash main.sh```

____

# Current Status

- Initialized Repository 
- Set up basic structure of Project 
- Implemented ```main.sh```