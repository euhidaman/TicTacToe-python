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

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

display_board()