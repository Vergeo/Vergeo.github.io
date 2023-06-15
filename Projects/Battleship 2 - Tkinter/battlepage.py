import tkinter as tk

class BattlePage(tk.Frame) :
	def __init__(self, parent, App) :
		self.settings = App.settings
		super().__init__(parent)
		self.pack(fill="both", expand=True)
		self.App = App

		self.board = ""

		self.mainframe = tk.Frame(self,bg = "gray")
		self.mainframe.pack(expand=True, fill="both")

		self.pixel = tk.PhotoImage(width=1,height=1)

		self.RB_row = []
		self.RB_col = []
		self.row_int = tk.IntVar()
		self.col_int = tk.IntVar()

		self.show_battleship_label()
		self.show_board()
		self.user_input()

	def show_battleship_label(self) :
		self.L_battleship = tk.Label(self.mainframe,bg="gray", text="Battleship",font=("Arial",30,"bold"))
		self.L_battleship.pack()

	def show_board(self) :
		self.F_board = tk.Frame(self.mainframe,bg="gray")
		self.F_board.pack()

		#print(self.App.battleship.board)
		for i in range(self.settings.row_board) :
			for j in range(self.settings.col_board) :
				if j == self.settings.col_board-1 :
					self.board += f"{self.App.battleship.board[i][j]}"
				else :
					self.board += f"{self.App.battleship.board[i][j]} "
			if i == self.settings.row_board-1 :
				pass
			else :
				self.board += "\n"

		self.L_board = tk.Label(self.F_board,text=f"{self.board}", font=("Arial",30), bg="gray40", fg="white")
		self.L_board.pack(pady=10)

	def update_board(self) :
		self.board = ""
		for i in range(self.settings.row_board) :
			for j in range(self.settings.col_board) :
				if j == self.settings.col_board-1 :
					self.board += f"{self.App.battleship.board[i][j]}"
				else :
					self.board += f"{self.App.battleship.board[i][j]} "
			if i == self.settings.row_board-1 :
				pass
			else :
				self.board += "\n"
		self.L_board.configure(text=self.board)
		self.L_board.pack(pady=10)

	def check(self) :
		self.UI_row = self.row_int.get()
		self.UI_col = self.col_int.get()


	def user_input(self) :
		F_UI = tk.Frame(self.mainframe,bg="gray30")
		F_UI.pack(fill="both",expand=True)

		# L_row = tk.Label(F_UI, text="Row  ", font=("Arial",30, "bold"),bg="gray30", fg="white")
		# L_row.grid(row= 0)

		# for i in range(self.settings.row_board) :
		# 	RB = tk.Radiobutton(F_UI, text=i+1, variable=self.row_int, value=i+1, font=("Arial",20,"bold"), bg="gray30",indicatoron=0,width=30,height=30, image=self.pixel,compound="c", fg="gray90")
		# 	RB.grid(padx=3,row=0, column=i+1)
		# 	self.RB_row.append(RB)

		# L_col = tk.Label(F_UI, text="Col  ", font=("Arial",30, "bold"),bg="gray30", fg="white")
		# L_col.grid(row= 1)
				
		# for i in range(self.settings.col_board) :
		# 	RB2 = tk.Radiobutton(F_UI, text=i+1, variable=self.col_int, value=(i+1), font=("Arial",20,"bold"), bg="gray30",indicatoron=0,width=30,height=30, image=self.pixel,compound="c", fg="gray90")
		# 	RB2.grid(padx=3,row=1, column=i+1)
		# 	self.RB_col.append(RB)

		# B_guess = tk.Button(F_UI, text="Guess", image=self.pixel,width=200, height=30, compound="c")
		# B_guess.grid(row=2, columnspan=6)

		F_row = tk.Frame(F_UI,bg="gray30")
		F_row.pack()

		L_row = tk.Label(F_row, text="Row  ", font=("Arial",30, "bold"),bg="gray30", fg="white")
		L_row.pack(side="left")

		for i in range(self.settings.row_board) :
			RB = tk.Radiobutton(F_row, text=i+1, variable=self.row_int, value=i+1, font=("Arial",20,"bold"), bg="gray30",indicatoron=0,width=30,height=30, image=self.pixel,compound="c", fg="gray90", command=self.check)
			RB.pack(padx=3,side="left")
			self.RB_row.append(RB)

		F_col = tk.Frame(F_UI,bg="gray30")
		F_col.pack()

		L_col = tk.Label(F_col, text="Col  ", font=("Arial",30, "bold"),bg="gray30", fg="white")
		L_col.pack(side="left")
				
		for i in range(self.settings.col_board) :
			RB2 = tk.Radiobutton(F_col, text=i+1, variable=self.col_int, value=(i+1), font=("Arial",20,"bold"), bg="gray30",indicatoron=0,width=30,height=30, image=self.pixel,compound="c", fg="gray90", command=self.check)
			RB2.pack(padx=3,side="left")
			self.RB_col.append(RB)

		B_guess = tk.Button(F_UI, text="Guess", font=("",10,"bold"), image=self.pixel,width=200, height=30, compound="c",command=self.App.check_UI)
		B_guess.pack(pady=3)