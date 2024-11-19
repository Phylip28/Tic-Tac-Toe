# Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game in Python where you play against the computer.

## Features

- Interactive command-line interface
- Player vs Computer gameplay
- Tutorial mode with instructions
- Random computer moves
- Visual game board representation
- Input validation and error handling
- Spanish language interface

## Requirements

- Python 3.x
- Standard Python libraries:
  - `random`
  - `time`

## How to Play

1. Run the game:
```bash
python tictactoe.py
```

2. Choose from the main menu options:
   - 1: Start game
   - 2: How to play
   - 3: Exit game

3. If you start a game:
   - Enter your name when prompted
   - Choose a position (1-9) on your turn
   - The computer will make its move automatically
   - Try to get three in a row to win!

## Game Rules

- The board has 9 squares numbered from 1 to 9
- You play as 'O', the computer plays as 'X'
- Take turns placing your symbol on the board
- First to get three in a row (horizontally, vertically, or diagonally) wins
- If all squares are filled and no one has won, it's a tie

## Board Layout
```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

## Functions

- `crear_tablero()`: Creates the initial game board
- `estado_del_tablero(board)`: Displays the current game board
- `movimiento_usuario(board, name)`: Handles player moves
- `movimiento_maquina(board)`: Handles computer moves
- `campos_libres(board)`: Checks for available moves
- `verificar_tablero(board, sign)`: Checks for win conditions
- `resultado(board, sign)`: Determines game outcome
- `instrucciones()`: Shows game tutorial

## Contributing

Feel free to fork this repository and submit pull requests with improvements!

## License

This project is open source and available under the MIT License.
