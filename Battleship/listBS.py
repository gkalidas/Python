#Create a variable board and set it equal to an empty list.

#2
#Create a 5 x 5 grid initialized to all 'O's and store it in board.
#use range() to loop 5 times.
#Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.
#Note that these are capital letter "O" and not zeros.

#3
#First, delete your existing print statement.
#Then, define a function named print_board with a single argument, board_in.
#Inside the function, write a for loop to iterates through each row in board and print it to the screen.
#Call your function with board to make sure it works.

#4
#Inside your function, inside your for loop, use " " as the separator to .join the elements of each row.

#1
board = []

#2
for i in range(5):
	board.append('O' * 5)

#3	
def print_board(board_in):
	for x in board_in:
		print " ".join(x)
		
print_board(board)

#4
