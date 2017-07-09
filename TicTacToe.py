# Sharon Gao
# April 2017
# Tic Tac Toe <Python>
from __future__ import print_function
from IPython.display import clear_output
import random

# METHOD print_board: Displays current board state.
def print_board(board):
    clear_output()
    print('      |      |      ')
    print('  ' + board[0] + '   |  ' + board[1] + '   |   ' + board[2] + '   ')
    print('______|______|______')
    print('      |      |      ')
    print('  ' + board[3] + '   |  ' + board[4] + '   |   ' + board[5] + '   ')
    print('______|______|______')
    print('      |      |      ')
    print('  ' + board[6] + '   |  ' + board[7] + '   |   ' + board[8] + '   ')
    print('      |      |      ')

# METHOD is_free: Boolean to determine if a space is occupied or not.
def is_free(board, position):
    return board[position] == ' '

# METHOD player_input: Accepts player input for board markers. Player inputs the corresponding character to place his or her 
# respective marker in a particular area of the board.
# Player controls:      
#  Q | W | E             
# ----------            
#  A | S | D             
# ----------              
#  Z | X | C             
def player_input(player, board):
    player_controls = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c'] # list of player controls
    position = ''
    if player == 1:
        marker = 'O'
        while position not in player_controls: 
            position = raw_input('Make your move, Player 1: ')
        while not is_free(board, player_controls.index(position)): # if position is already occupied
            position = raw_input('That square is occupied! Pick another: ')
            if position not in player_controls:
                while position not in player1:
                    position = raw_input('Invalid input! Choose a space using "Q", "W", "E", "A", "S", "D", "Z", "X", or "C": ')
        board[player_controls.index(position)] = marker
    elif player == 2:
        marker = 'X'
        while position not in player_controls: 
            position = raw_input('Make your move, Player 2:')
        while not is_free(board, player_controls.index(position)): # if position is already occupied
            position = raw_input('That square is occupied! Pick another: ')
            if position not in player_controls:
                while position not in player_controls:
                    position = raw_input('Invalid input! Choose a space using "Q", "W", "E", "A", "S", "D", "Z", "X", or "C": ')
        board[player_controls.index(position)] = marker
        
# METHOD check_win: Checks board state to see if there is a winner and returns a boolean. A player wins by having 3 marks in a 
# line horizontally, vertically, or diagonally. The game ends as soon as a player has 3 marks in a row.
def check_win(board, mark):
    return ((mark == board[0] and mark == board[1] and mark == board[2]) or # horizonatal win, top row
    (mark == board[3] and mark == board[4] and mark == board[5]) or # horizonatal win, middle row
    (mark == board[6] and mark == board[7] and mark == board[8]) or # horizonatal win, bottom row
    (mark == board[0] and mark == board[3] and mark == board[6]) or # vertical win, left column
    (mark == board[1] and mark == board[4] and mark == board[7]) or # vertical win, middle column
    (mark == board[2] and mark == board[5] and mark == board[8]) or # vertical win, right column
    (mark == board[0] and mark == board[4] and mark == board[8]) or # diagonal win, top left to bottom right
    (mark == board[2] and mark == board[4] and mark == board[6])) # diagonal win, top right to bottom left

# METHOD board_full: Checks if board is full and returns a boolean.
def board_full(board):
    for space in range(0, 9):
        if is_free(board, space):
            return False
    return True

# METHOD replay: Asks the player if they want to play another round. 'Y' starts another game, 'N' ends the program.
def replay():
    return (raw_input("Play another round? ('Y' to continue, 'N' to quit): ").lower() == 'y')

print('Welcome to Tic Tac Toe!')
print('Player 1 will be "O", Player 2 will be "X".')
print('Player Controls:')
print('  Q  |  W  |  E ')
print('-----------------')
print('  A  |  S  |  D ')
print('-----------------')
print('  Z  |  X  |  C ')



while True:
    gameBoard = [' '] * 10
    flip = random.randint(0, 1)
    currentPlayer = 0
    if flip == 0:
        print('Player 1 goes first!')
        currentPlayer = 1
    else:
        print('Player 2 goes first!')
        currentPlayer = 2
    cont = True
    while cont: 
        if currentPlayer == 1:
            print_board(gameBoard)
            player_input(currentPlayer, gameBoard)
            if check_win(gameBoard, 'O'):
                print_board(gameBoard)
                print('Player 1 wins!')
                cont = False
            else:
                if board_full(gameBoard):
                    print_board(gameBoard)
                    print('The game is a Tie!')
                    break
                else:
                    currentPlayer = 2
        elif currentPlayer == 2:
            print_board(gameBoard)
            player_input(currentPlayer, gameBoard)
            if check_win(gameBoard, 'X'):
                print_board(gameBoard)
                print('Player 2 wins!')
                cont = False
            else:
                if board_full(gameBoard):
                    print_board(gameBoard)
                    print('The game is a Tie!')
                    break
                else:
                    currentPlayer = 1
    if not replay():
        break
