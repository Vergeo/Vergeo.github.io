
class Config :
	def __init__(self) :
		# Game Config
		self.title = "Battleship"
		self.row = 5
		self.column = 5

		# Window Config
		base = 100
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+250+50"

		# Image Path
		self.init_img="image/bomb.png"
		self.final_img="image/zonk.png"
		self.win_img="image/Success.png"