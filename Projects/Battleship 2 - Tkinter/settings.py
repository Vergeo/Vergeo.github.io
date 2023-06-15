class Settings :
	def __init__(self) :
		# self.w_ratio = 4
		# self.h_ratio = 3
		# self.base = 200
		# self.width = self.w_ratio*self.base
		# self.height = self.h_ratio*self.base
		# self.screen = f"{self.width}x{self.height}+250+50"

		self.title = "Battleship"

		self.row_board = 8
		self.col_board = 8

		self.screen =f"{self.row_board*100}x{self.col_board*100-200}+250+50"