# Command Line Tic Tac Toe Game

A Python implementation of the classic Tic Tac Toe game that runs in the command line.

## Description

This is a simple command-line based Tic Tac Toe game written in Python. Players take turns to place their marks ('X' or 'O') on a 3x3 grid, with the goal of getting three of their marks in a horizontal, vertical, or diagonal row.

## Features

- Easy-to-use command-line interface
- Players can choose to play as 'X' or 'O'
- Colorful game board and text using the colorama library
- Win detection for horizontal, vertical, and diagonal lines
- Draw detection when the board is full with no winner
- Option to restart the game or exit after completion

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/command-line-tic-tac-toe.git
   cd command-line-tic-tac-toe
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Dependencies

- Python 3.6 or higher
- colorama - For colored text output
- mock - For running tests

## Usage

To start the game, run:
```
python main.py
```

### How to Play

1. The first player chooses whether to play as 'X' or 'O'.
2. Players take turns entering a number (1-9) corresponding to the position on the board where they want to place their mark.
3. The game ends when a player gets three marks in a row (horizontally, vertically, or diagonally) or when the board is full (a draw).
4. After the game ends, you can choose to restart or exit.

### Game Board Layout

The positions on the board are numbered as follows:
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

## Project Structure

```
tic-tac-toe/
│
├── main.py               # Main game entry point
├── requirements.txt      # Project dependencies
├── LICENSE               # GNU GPL v3 license
│
├── tic_tac_toe/          # Game module package
│   ├── __init__.py
│   ├── game.py           # Game class definition and logic
│   └── player.py         # Player class definition and logic
│
└── test/                 # Test package
    ├── __init__.py
    ├── test_game.py      # Tests for game module
    ├── test_main.py      # Tests for main module
    └── test_player.py    # Tests for player module
```

## Testing

Run all tests with:
```
python -m unittest
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## Acknowledgments

- Created as a Python programming exercise
- Inspiration from the classic Tic Tac Toe game
