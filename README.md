#Snake Game

A classic Snake game built in Python using the built-in `turtle` graphics library. The game recreates the traditional Snake experience with smooth movement, randomly spawning food, score tracking, snake growth, collision detection, and persistent high scores.

This project was developed to strengthen my understanding of object-oriented programming, event-driven programming, and game development fundamentals in Python.

---

## Features

* Classic Snake gameplay
* Smooth snake movement using keyboard controls
* Randomly generated food locations
* Snake grows after eating food
* Real-time score tracking
* Persistent high score saved between game sessions
* Collision detection with walls
* Collision detection with the snake's own body
* Automatic game reset after collisions

---

## Technologies Used

* Python 3
* Turtle Graphics
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
snake_game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
└── README.md
```

### File Overview

### `main.py`

* Creates the game window
* Runs the main game loop
* Handles keyboard input
* Detects collisions between the snake, food, walls, and tail
* Coordinates interactions between all game objects

### `snake.py`

* Implements the `Snake` class
* Controls movement and direction changes
* Handles snake growth after eating food
* Resets the snake after collisions

### `food.py`

* Implements the `Food` class
* Randomly generates food positions within the game area

### `scoreboard.py`

* Displays the current score
* Loads and saves the high score using `data.txt`
* Updates the scoreboard after scoring or resetting

### `data.txt`

* Stores the highest score so it persists between game sessions

---

## Controls

| Key | Action     |
| --- | ---------- |
| ↑   | Move Up    |
| ↓   | Move Down  |
| ←   | Move Left  |
| →   | Move Right |

---

## How to Run

### Requirements

* Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/snake_game.git
```

Navigate to the project folder:

```bash
cd snake_game
```

Run the game:

```bash
python main.py
```

---

## Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Class design and modular programming
* Event-driven programming
* Game loop implementation
* Collision detection
* Keyboard event handling
* Random number generation
* File input/output
* Persistent data storage

---

## Future Improvements

* Main menu
* Pause and resume functionality
* Multiple difficulty levels
* Sound effects
* Different food types
* Obstacles
* Power-ups
* Animated game-over screen
* Improved graphics using Pygame

---

## Author

**Tobit Vervat**
