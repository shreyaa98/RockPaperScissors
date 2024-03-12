# RockPaperScissors
This Python program implements a simple game of Rock, Paper, Scissors (RPS) with a graphical user interface using Tkinter and Pygame animations. The game allows a player to compete against a computer opponent by selecting one of the three options: rock, paper, or scissors. The winner is determined based on the traditional rules of RPS.

## Features
1. Graphical User Interface (GUI): Utilizes Tkinter for interactive gameplay.
2. Player vs. Computer: Allows players to compete against the computer.
3. Animation: Features animated GIFs for visual appeal.
4. Sound Effects: Incorporates sound effects for various actions.
5. Score Tracking: Dynamically updates player and computer scores.
6. Winner Determination: Follow traditional RPS rules to determine winners.
7. Final Message Display: Shows winner or tie message at the end of each round.
8. Responsive Design: Adapts to different screen sizes.
9. Error Handling: Includes basic error handling for smooth execution.
10. Customizable Assets: Allows images, sounds, and animation customization.

## Files
1. RPS_Main.py contains the main code for the game.
2. rock.png, paper.png, and scissors.png are images representing the rock, paper, and scissors icons used in the game.
3. You-Default-IMage.png and Bot-Default-IMage.png are the default images for the player and the bot.
4. r_user.png, r_bot.png, p_user.png, p_bot.png, s_user.png, s_bot.png: Images representing different gestures of the player and the bot (rock, paper, scissors).
5. celebration.gif animation file for celebration.
6. tie.png indicating a tie.
7. click.wav, you_win.wav, bot_win.wav, bg_music.mp3: Sound files used in the game for various actions.
8. bg.gif: Background animation

## Technical Aspects
Build Management and Automated TestCases are done using GitHub Actions.

## Dependencies:
1. Python 3.11.5
2. Pygame
3. Tkinter (usually comes pre-installed with Python)
4. PIL (Python Imaging Library)
5. flake8 (For Python Style Checks)

## Installation
1. Clone the repository: https://github.com/shreyaa98/RockPaperScissors.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the game: python celebration.py

## Instructions to Play the Game 
1. Run the script.
2. Click on the "PLAY!" button to start the game.
3. Choose Rock, Paper, or Scissors by clicking the corresponding button.
4. The computer will randomly select its choice.
5. The winner is determined based on the rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
6. See the outcome of the game and the updated scores.
7. Enjoy the game!

## Class Diagram
The class diagram depicts the relationships and structure of classes in the Rock, Paper, Scissors game, illustrating how the RPSGame class orchestrates the game functionality while utilizing the RPSImageLoader class for image loading and Tkinter for the graphical user interface.

**[Class Diagram](https://github.com/shreyaa98/RockPaperScissors/blob/3329792940fb2a04320fd1b399642767cd64d2ee/Class%20Diagram%20Shreya.png)**

## Sequence Diagram 
A sequence diagram illustrates the flow of interactions and events between different components or actors in a system or process, typically depicted in a diagrammatic format.

**[Sequence Diagram](https://github.com/shreyaa98/RockPaperScissors/blob/3329792940fb2a04320fd1b399642767cd64d2ee/Sequence%20Diagram%20Shreya.png)**

## State Diagram
The state diagram represents the different states and transitions of the Rock, Paper, Scissors game, illustrating the flow of actions and decisions from player input to game outcomes

**[State Diagram](https://github.com/shreyaa98/RockPaperScissors/blob/3329792940fb2a04320fd1b399642767cd64d2ee/State%20Diagram%20Shreya.png)**

## Note:
1. Ensure that all dependencies are installed properly to run the game without errors.
2. Ignore the Pygame window 
