import tkinter as tk
from PIL import Image, ImageTk


class Board(tk.Frame) :
	def __init__(self, parent, Game) :
		self.game = Game
		self.config = Game.config

		# Config Frame
		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0,column=1,sticky="nsew")
		parent.grid_rowconfigure(0, weight =1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_mainframe()
		self.create_board()
		self.show_board()

		# Config Button
		self.pixel = tk.PhotoImage(width=1,height=1)

		self.create_buttons()
		self.show_buttons()

	def create_mainframe(self) :
		self.mainframe = tk.Frame(self, height = self.config.side, width = self.config.side, bg="black")
		self.mainframe.pack(expand=True)

	def create_board(self) :
		self.frame_rows = []

		color = 756867
		n_row, n_column = self.config.row,self.config.column
		row_height, row_width = self.config.side//n_row, self.config.side

		for i in range(n_row) :
			row_color = f"#{color}"
			frame=tk.Frame(self.mainframe, height=row_height, width = row_width, bg=row_color)
			self.frame_rows.append(frame)
			color += 500


	def show_board(self) :
		for frame in self.frame_rows :
			frame.pack()

	def resize_photo(self, ori_image, scale) :
		n_column = self.config.column
		button_width = self.config.side//n_column-8

		image = Image.open(ori_image)
		image_w, image_h = image.size
		ratio = image_w/self.config.side

		image = image.resize((int(image_w//ratio//scale), int(image_h//ratio//scale)))
		return ImageTk.PhotoImage(image)

	def create_buttons(self) :
		self.logo = self.resize_photo(self.config.init_img,7)
		self.guess = self.resize_photo(self.config.final_img,7)
		self.correct = self.resize_photo(self.config.win_img,5)

		self.buttons_board = []
		n_row, n_column = self.config.row,self.config.column
		button_height, button_width = self.config.side//n_row-8, self.config.side//n_column-8
		for i in range(n_row) :
			row=[]
			for j in range(n_column) :
				button = tk.Button(self.frame_rows[i], image =self.logo, width=button_width, height = button_height, bg="gray20",text=" ",compound="c", font=("Arial",36,"bold"), fg="white", command=lambda i=i,j=j:self.game.change_picture(i,j))
				row.append(button)
			self.buttons_board.append(row)
		print(row)

	def show_buttons(self) :
		n_row, n_column = self.config.row,self.config.column

		for i in range(n_row) :
			for j in range(n_column) :
				self.buttons_board[i][j].pack(side="left")
