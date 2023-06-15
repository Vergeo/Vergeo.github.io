from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.animation import Animation

import bcrypt

class Geschenk(MDApp) :
	def __init__(self) :
		super().__init__()
		self.title = "Geschenk"

		self.screen_manager = ScreenManager()
		self.add_pages("page.kv")
		self.make_page()

	def add_pages(self, path) :
		self.screen_manager.add_widget(Builder.load_file(path))

	def on_start(self) :
		self.screen_manager.current = "page"

	def build(self) :
		return self.screen_manager

	def make_page(self) :
		main_layer = MDFloatLayout(md_bg_color=(0,0,0,1), size_hint=(1,1), pos_hint={"center_x" : .5, "center_y" : .5})
		self.layers = []
		menus = [(1, "a"),(2, "b"),(3, "c"),(4, "d"),(5, "e"),(6, "f"),]
		counter = len(menus)

		main_layer.size_hint = (1, counter/5)

		for i in range(counter-1, -1, -1) :
			layer = MDBoxLayout(md_bg_color=(i/10,(i+1)/20,0,1), size_hint=(1, 1/counter), pos_hint = {"center_x" : 0.5, "center_y" : ((1/counter*(i+1))-1/counter/2)})
			layer.add_widget(Label(text=menus[i][1]))
			main_layer.add_widget(layer)
			self.layers.append(layer)

		# for layer in self.layers :
		# 	main_layer.add_widget(layer)

		self.screen_manager.screens[0].ids["scrl_view"].add_widget(main_layer)


		# self.text_label = Label(text="Waiting for Button Pressed")

		# button0 = Button(text="Click Me")
		# # button0.bind(on_press=self.button0_press)
		# button1 = Button(text="Click Me")
		# # button0.bind(on_press=self.button1_press)

		# self.text_input0 = TextInput(text="Text Input")
		# self.text_input1 = TextInput(text="Text Input")

		# boxlayout_h0 = BoxLayout(orientation="horizontal")
		# boxlayout_h1 = BoxLayout(orientation="horizontal")

		# boxlayout_main = BoxLayout(orientation="vertical")

		# boxlayout_h0.add_widget(widget=self.text_input0)
		# boxlayout_h0.add_widget(widget=button0)

		# boxlayout_h1.add_widget(widget=self.text_input1)
		# boxlayout_h1.add_widget(widget=button1)

		# boxlayout_main.add_widget(widget=self.text_label)
		# boxlayout_main.add_widget(widget=boxlayout_h0)
		# boxlayout_main.add_widget(widget=boxlayout_h1)
		# self.screen_manager.screens[0].ids["scrl_view"].add_widget(boxlayout_main)

if __name__ == "__main__" :
	app = Geschenk()
	app.run()