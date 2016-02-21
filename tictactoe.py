import random

#the board
board = [0,1,2,
	3,4,5,
	6,7,8]

def show():
	print(board[0] ,'|' , board[1],'|',board[2])
	print('----------')
	print(board[3] ,'|' , board[4],'|',board[5])
	print('----------')
	print(board[6] ,'|' , board[7],'|',board[8])

show()

while True:
	spot = input("select a spot:")
	spot = int(spot)

	if board[spot] !='x' and board[spot]!= 'o':
		board[spot] = 'x'  
		
		#available = True
		
		while True:
			random.seed()
			opponent = random.randint(0,8)
		
			if board[opponent] != 'o' and board[opponent]!= 'x':
				board[opponent] = 'o'
				#available = False
				break;
	 
	else:
		print("This is already taken!")

	show()

