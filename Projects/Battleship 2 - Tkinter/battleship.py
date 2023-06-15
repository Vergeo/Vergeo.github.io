from random import randint

class Ship :
	def __init__(self, App) :
		self.settings = App.settings
		self.row = self.settings.row_board
		self.col = self.settings.col_board

		self.create_board()
		self.get_random_ship()

	def create_board(self) :
		self.board = []
		for i in range(self.row) :
			self.board.append(["O"]*self.col)

		# print(self.board) ○
	
	def get_random_ship(self) :
		(self.s_row, self.s_col) = (randint(1,self.settings.row_board),randint(1,self.settings.col_board))
		#print(self.s_row, self.s_col)