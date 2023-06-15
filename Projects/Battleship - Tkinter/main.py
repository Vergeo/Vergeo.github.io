import tkinter as tk

from config import Config
from board import Board
from player import Player
from ship import Ship

class Window(tk.Tk) :
	def __init__ (self, Game) :
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}

		self.create_board()

	def create_container(self) :
		self.container = tk.Frame(self, bg="gray20")
		self.container.pack(fill="both",expand=True)

	def create_board(self) :
		self.pages["Board"] = Board(self.container,self.game)

class Battleship :
	def __init__(self) :
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)
		self.win = False

	def check_location(self) :
		if self.ship.location == self.player.location :
			return True
		return False

	def change_picture(self, x,y) :
		if self.win == False :
			self.window.pages["Board"].buttons_board[x][y].configure(image=self.window.pages["Board"].guess)
			self.player.current_location(x,y)
			self.window.pages["Board"].show_buttons()
			self.win = self.check_location()
			if self.win :
				self.window.pages["Board"].buttons_board[x][y].configure(image=self.window.pages["Board"].correct)
				self.window.pages["Board"].show_buttons()			

	def run(self) :
		self.window.mainloop()


def main() :
	my_battleship = Battleship()
	my_battleship.run()

if __name__ == "__main__" :
	main()