import tkinter as tk
from settings import Settings
from battlepage import BattlePage
from battleship import Ship

class MainWindow(tk.Tk) :
	def __init__(self, App) :
		self.settings = App.settings
		super().__init__()

		self.title(self.settings.title)
		self.geometry(self.settings.screen)

		self.create_Container()
		self.pages = {}
		self.create_Battleship()
		self.create_BattlePage()

	def create_Container(self) :
		self.container = tk.Frame(bg="grey")
		self.container.pack(fill="both", expand = True)

	def create_BattlePage(self) :
		self.pages["BattlePage"] = BattlePage(self.container,self)

	def create_Battleship(self) :
		self.battleship = Ship(self)

	def check_UI(self) :
		self.s_row = self.battleship.s_row
		self.s_col = self.battleship.s_col
		self.UI_row = self.pages["BattlePage"].UI_row
		self.UI_col =self.pages["BattlePage"].UI_col
		print(self.s_row,self.s_col,self.UI_row,self.UI_col)

		if self.UI_row == self.s_row and self.UI_col == self.s_col :
			self.battleship.board[self.UI_row-1][self.UI_col-1] = "✓"
			self.pages["BattlePage"].L_board.configure(fg="green")
			self.pages["BattlePage"].update_board()
		else :
			self.battleship.board[self.UI_row-1][self.UI_col-1] = "X"
			self.pages["BattlePage"].update_board()

		#×

class App :
	def __init__(self) :
		self.settings = Settings()
		self.main_window = MainWindow(self)

	def run(self) :
		self.main_window.mainloop()

if __name__ == "__main__" :
	My_app = App()
	My_app.run()