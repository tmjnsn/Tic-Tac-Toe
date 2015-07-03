import os
import sys
# Tic-Tac-Toe by Tim Jansen

# Board layout:
# |1|2|3|
# |4|5|6|
# |7|8|9|

board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
win_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
wins_x = 0
wins_o = 0
previous_game_starter = 'O'
turn = ''

def initial_setup():
    """ Chooses who starts the game and displays starter message """
    global previous_game_starter
    global turn
    
    if previous_game_starter == 'O':
        previous_game_starter = 'X'
        turn = 'X'
    else:
        previous_game_starter = 'O'
        turn = 'O'
    print '\nThis Tim\'s Tic-Tac-Toe game for 2 players'
    print 'The board is numbered like this:'
    print '-------------'
    print '| 1 | 2 | 3 |'
    print '-------------'
    print '| 4 | 5 | 6 |'
    print '-------------'
    print '| 7 | 8 | 9 |'
    print '-------------'
    print 'When it\'s your turn, pick a number to fill in that field'
    print 'Player ' + turn + ' will start this game'
    print 'Have fun!\n'

def main():
    """ Main loop """
    global board
    global turn
    
    initial_setup()
    move_count = 0
    while move_count < 9:
        valid_input = False
        while(valid_input == False):
            move = input('It\'s player ' + turn + '\'s turn. What is your move?: ')
            if is_position_valid(move):
                valid_input = True
                board[move] = turn
            else:
                print 'That is an invalid move'
        
        print_board()
        win_result = check_win()
        if win_result != None:
            print '############# Player ' + win_result + ' has won the game! #############'
            print_total_score()
            ask_restart()
            
        move_count = move_count + 1
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    print '############# Tie #############'
    print_total_score()
    ask_restart()

def print_total_score():
    """ Prints the total amount of wins for each player """
    global wins_x
    global wins_o
    
    print 'Total score:'
    print 'Player X: ' + str(wins_x)
    print 'Player O: ' + str(wins_o)
            
def is_position_valid(pos):
    """ Checks if the entered position is on the board and emtpy """
    global board
    
    if pos in range(1,10):
        if board[pos] != ' ':
            return False
        else:
            return True
    else:
        return False

def print_board():
    """ Prints the current status of the tic-tac-toe board """
    global board
    
    print '-------------'
    line = '| '
    for k, v in board.items():
        line = line + v + ' | '
        if k % 3 == 0:
            print line
            print '-------------'
            line = '| '
    
def check_win():
    """ Checks if there is a winner. If there is, returns the winner. If there isn't, returns None """
    global wins_x
    global wins_o
    global board
    global win_combos
    
    for win_combo in win_combos:
        if (
            board[win_combo[0]] != ' ' 
            and board[win_combo[0]] == board[win_combo[1]] 
            and board[win_combo[0]] == board[win_combo[2]]
        ):
            if board[win_combo[0]] == 'X':
                wins_x = wins_x + 1
                return 'X'
            else:
                wins_o = wins_o + 1
                return 'O'
    return None

def ask_restart():
    """ Asks the player(s) if they want to play another game """
    game_restart_input = raw_input('Play another game? Y/N: ').lower()
    if game_restart_input == 'y' or game_restart_input == 'yes':
        restart_game()
    elif game_restart_input == 'n' or game_restart_input == 'no':
        sys.exit()
    else:
        print 'That is not a valid input'

def restart_game():
    """ Restarts the game """
    global board
    
    os.system('cls')
    #clear()
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    main()

main()