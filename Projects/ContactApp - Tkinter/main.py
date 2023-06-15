import tkinter as tk

from settings import Settings
from appPage import AppPage

class Window(tk.Tk) :
	def __init__(self,app) :
		self.app = app
		self.settings = Settings()
		super().__init__()

		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_containter()

		self.pages = {}
		self.create_appPage()

	def create_containter(self) :
		self.container = tk.Frame(self)
		self.container.pack(fill="both",expand=True)

	def create_appPage(self) :
		self.pages["appPage"] = AppPage(self.container, self.app)


class ContactApp :
	def __init__(self) :
		self.settings = Settings()
		self.main_window = Window(self)

	def run(self) :
		self.main_window.mainloop()

if __name__ == "__main__" :
	App = ContactApp()
	App.run()