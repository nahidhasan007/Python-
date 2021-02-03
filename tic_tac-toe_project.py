board = ['-','-','-','-','-','-','-','-','-']

game_still_going = True

winner = None

current_player = 'X'
def display_board():
	print(board[0] + '|' + board[1] + '|' + board[2])
	print(board[3] + '|' + board[4] + '|' + board[5])
	print(board[6] + '|' + board[7] + '|' + board[8])

def play_game():

	display_board()

	while game_still_going:

		handle_turn(current_player)

		check_if_game_over()

		flip_player()
	if winner =='X' or winner =='O':
		print(winner + ' won the game')
	elif winner == None:
		print('its a tie')	
       


def flip_player():
	global current_player
	if current_player=="X":
		current_player="O"
	elif current_player=="O":
		current_player="X"
	return	


def check_if_game_over():
	
	check_for_winner()

	check_if_tie()

def check_for_winner():
	
	#check rowa
	#check columns
	#check diagonal
	global winner

	row_winner = check_for_rows()

	column_winner = check_for_column()

	diagonal_winner = check_for_diagonal()

	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None
	return	
							
def check_for_rows():
	global game_still_going
	row1 = board[0]==board[1]==board[2]!='-'
	row2 = board[3]==board[4]==board[5]!='-'
	row3 = board[6]==board[7]==board[8]!='-'
	if row1 or row2 or row3:
		game_still_going = False
	if row1:
		return board[0]
	elif row2:
		return board[3]
	elif row3:
		return board[6]				
	return


def check_for_column():
	global game_still_going

	column1 = board[0]==board[3]==board[6]!='-'
	column2 = board[1]==board[4]==board[7]!='-'
	column3 = board[2]==board[5]==board[8]!='-'

	if column1 or column2 or column3:
	   game_still_going = False

	if column1:
		return board[0]
	elif column2:
		return board[1]
	elif column3:
		return board[2]	   
	return

def check_for_diagonal():
	global game_still_going

	diagonal1 = board[0]==board[4]==board[8]!='-'
	diagonal2 = board[2]==board[4]==board[6]!='-'

	if diagonal1 or diagonal2:
		game_still_going = False

	if diagonal1:
		return board[0]
	elif diagonal2:
		return board[2]				
	return	


	return
def check_if_tie():
	global game_still_going
	if '-' not in board:
		game_still_going = False
	return				


		

###def handle_turn(player):
   ### global current_player
	#board_position = input('choose a position from board : ')

	#board_position = int(board_position)-1

	#board[board_position] = player

	#display_board()
##def handle_turn(player):
	##global current_player
	###sotti = False
	#print(current_player + "'s turn.")
	#board_position = input('choose a position from the board: ')
	#while not sotti:
		#while board_position not in ['1','2','3','4','5','6','7','8','9']:
	    #board_position = int(board_position)-1
	   # if board[board_position] !='-':
def handle_turn(player):
	global current_player

	print(current_player + "'s turn")

	board_position = input('choose a position from the board: ')

	board_position = int(board_position)-1

	board[board_position] = player

	display_board()
play_game()	

