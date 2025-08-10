A tic-tac-toe game to practice dictionaries  
and code reading  
Users shall be presented with this board:  
  a   b   c  
1 - | - | -  
2 - | - | -  
3 - | - | -  

1. For a given input, say "1, a" use a translation  
dictionary to translate to coordinates (say 0, 0)  
from https://gist.github.com/rafrafavi/97e22d5ea4533080d7d94c4fa430d2b4  

```python
translation = {"cols": {}, # TODO: Complete me
               "rows": {}}

players = {"x_player": {"name": '',
                        "symbol": 'X',
                        "wins": 0,
                        "draws": 0,
                        "losses": 0},
            "o_player": {"name": '',
                         "symbol": 'O',
                         "wins": 0,
                         "draws": 0,
                         "losses": 0},
           "current_player": ''} # TODO: Use me!

WINS = [ # lists all win conditions for 3 x 3 board
    [(0,0), (1,1), (2,2)], # diag 1
    [(0,2), (1,1), (2,0)], # diag 2
    [(0,0), (0,1), (0,2)], # row 1
    [(1,0), (1,1), (1,2)], # row 2
    [(2,0), (2,1), (2,2)], # row 3
    [(0,0), (1,0), (2,0)], # col a
    [(0,1), (1,1), (2,1)], # col b
    [(0,2), (1,2), (2,2)], # col c
]
```

2. Optional task (challenging): generate the above list dynamically using for loops.
```python
def create_board():
    return [['-' for _ in range(3)]
            for _ in range(3)]


def print_board(board):
    print("  a   b   c")
    for i, row in enumerate(board, 1):
        print(i, end=' ')
        print(' | '.join(row))


def translate(row, col):
    """Returns corresponding position from dictionary"""
    # TODO: Finish this function so it returns the correct row, col
    # For example:
    # >>> translate('1', 'a') 
    # (0, 0)
    return ...


def has_free_spaces(board):
    for row in board:
        if '-' in row:
            return True
    return False


def is_occupied(board, coords):
    row, col = coords
    return '-' != board[row][col].strip()


def is_winner(x_or_o, board):
    for (row1, col1), (row2, col2), (row3, col3) in WINS:
        if (board[row1][col1] ==
            board[row2][col2] ==
            board[row3][col3] ==
            x_or_o):
            return True
    return False

def switch(current, p1, p2):
    if current == p1:
        return p2
    else:
        return p1


def set_position(x_or_o, board, coords):
    row, col = coords
    board[row][col] = x_or_o.upper()


def play():
    # TODO: Set player names in the players dictionary
    # TODO: Initialize current_player from the dictionary
    # TODO: Get the player name from the dictionary
    # TODO: Implement switching players using the players dictionary


    print("Welcome to Tic-Tac Life!")
    
    print("What shall I call the 'X' player?")
    name_x = input("Player X's name> ")
    
    print("and the 'O' player?")
    name_o = input("Player O's name> ")

    board = create_board()

    current_player = name_x
    symbol = 'X'

    while True:
        print(f"{current_player} make your move:")
        print_board(board)
        move = input("Enter move as i, c: ")
        row, col = move.replace(' ', '').split(',')
        row, col = translation["rows"][row], translation["cols"][col] # TODO: populate translation dict - otherwise this fails
        if is_occupied(board, (row, col)):
            print("You must pick an unused space")
            continue
        else:
            set_position(symbol, board, (row, col))
        if is_winner(symbol, board):
            print(f"Well done!\nPlayer {current_player} wins!")
            break
        if not has_free_spaces(board):
            print("It is a draw!")
            break

        current_player = switch(current_player, name_x, name_o)
        symbol = switch(symbol, 'X', 'O')

    # TODO: add ability to play again
    # TODO: keep tally of wins, losses, and draws in the dictionary
    # TODO: print the dictionary as a csv like so:
    # name,symbol,wins,draws,losses
    # fred,X,10,5,3
    # wilma,O,5,10,3
    # BONUS: instead of using csv, write the dictionary to a JSON file 
    # (clue: even though it is the bonus question, this is actually easier!)


play()
```