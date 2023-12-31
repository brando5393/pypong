# pyPong

Atari's arcade classic resurrected in python with some additional gameplay options.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [System-Requirements](#System-Requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [License](#license)

## Description:
pyPong is a two-player Pong game built using the pygame library. It features basic paddle movement, ball collision detection, score tracking, and powerups. This was built as a code along project following the YouTube video [Pong with Python & Pygame – Tutorial](https://www.youtube.com/watch?v=tS8F7_X2qB0) from [freeCodeCamp.org](freeCodeCamp.org)

All sound effects for the game were sourced from [https://soundbible.com/](https://soundbible.com/) and all credit for the sound effects goes to their respective creators. Direct links to the sound effects used are listed below:
- [Ball Hit](https://soundbible.com/1343-Jump.html#)
- [Smash Powerup](https://soundbible.com/670-Swooshing.html)
- [Flash Powerup](https://soundbible.com/2067-Blop.html)

## Features:
- Two-player Pong game
- Paddle movement using 'W'/'S' (Player 1) and arrow keys (Player 2)
- Ball collision detection
- Score tracking for both players
- Powerup system with smash and flash powerups
- Sound effects for ball collision, smash powerup, and flash powerup
- Random ball direction and angle on score
- Responsive UI with real-time updates

## System-Requirements
- Python 3.6 or higher
- [pygame](https://www.pygame.org/) library

## Installation:
1. Clone the repository:
```sh
   git clone https://github.com/brando5393/pyPong.git
```
2. Navigate to the project directory:
```sh
   cd pyPong
```
3. Install the required dependencies:
```sh
   pip install pygame
```
## Usage:
1. Run the game:
```sh
   python main.py
```
2. Play the game using the controls mentioned below.

3. The game window will display the player scores, powerup counts, and the Pong gameplay.

## Controls:
- Player 1 (Left Paddle):
  - Move Up: 'W' key
  - Move Down: 'S' key
  - Smash Powerup: 'D' key
  - Flash Powerup: 'A' key

- Player 2 (Right Paddle):
  - Move Up: Up Arrow
  - Move Down: Down Arrow
  - Smash Powerup: Right Arrow
  - Flash Powerup: Left Arrow

## License:
This project is licensed under the MIT License.
