# elements required-->
# board
# display board
# play game
# handle turn
# check win
  # -check row
  # -check column
  # -check diagonal
# check tie
# flip player


#------------GlobalVariable-------------
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if Game still goin on
game_still_going = True

# Who won ? or Tie?
winner = None

# Who's turn , is it?
current_player = "X"

# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# play game tic tac toe
def play_game():
    # display initial board
    display_board()

    # while the game is still going on
    while game_still_going:

        # handle a single turn of an arbitraray player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # the game has ended
    if winner =='X' or winner =='O':
        print(winner + ' won.')
    elif winner == None :
        print("Tie.")

# handle a single turn of an arbitraray player
def handle_turn(player):
    position = input("Choose a position from 1 to 9: ")
    position = int(position)-1

    board[position] = "X"
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # set up global variable
    global winner
    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner  = row_winner()
    elif column_winner:
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        # there was no win
        winner = None

    return

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_if_tie():
    return

def flip_player():
    return

play_game()
