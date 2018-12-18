#hiding the ship

#Define two new functions, random_row and random_col, that each take board_in as input.
#These functions should return a random row index and a random column index from your board, respectively.
#Use randint(0, len(board_in) - 1).
#Call each function on board.

from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board_in):
  return randint(0, len(board_in) - 1)
def random_col(board_in):
  return randint(0, len(board_in) - 1)

#taking guesses from the user
ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(raw_input("Guess Row :"))
guess_col = int(raw_input("Guess Col :"))
