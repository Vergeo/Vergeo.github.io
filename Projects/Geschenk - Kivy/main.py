from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.animation import Animation

from settings import Settings
import bcrypt
from models.user import User

LabelBase.register(name = "Barlow",
					fn_regular = "assets/font/Barlow-SemiBold.ttf",
					fn_bold = "assets/font/Barlow-Black.ttf")

class Geschenk(MDApp) :
	def __init__(self) :
		super().__init__()
		self.title = "Geschenk"
		self.settings = Settings()

		self.screen_manager = ScreenManager()
		self.add_pages("pages/splash.kv")
		self.add_pages("pages/login.kv")
		self.add_pages("pages/dashboard.kv")
		self.add_pages("pages/make_a_purchase2.kv")
		self.add_pages("pages/profile.kv")
		self.add_pages("pages/overview.kv")

		self.current_user = None
		self.purchase = {}
		self.layers = []
		self.labels = []
		self.items_in_lables = []

	def add_pages(self, path) :
		self.screen_manager.add_widget(Builder.load_file(path))

	def build(self) :
		self.icon = "assets/img/icon2.png"
		self.screen_manager.current = "splash"
		# self.screen_manager.current = "dashboard"

		# self.change_page("overview")
		return self.screen_manager

	def on_start(self) :
		Clock.schedule_once(lambda *args:self.change_page("login"), 3)

	def change_page(self, page, *args) :
		self.screen_manager.current = page
		if page == "login" :
			self.animate_subtitle(self.screen_manager.screens[1].ids["login_img"], 0)
		if page == "dashboard" :
			self.screen_manager.screens[2].ids["nav_drawer"].set_state("close")
			self.animate_subtitle(self.screen_manager.screens[2].ids["dashboard_img"], -.2)
			self.screen_manager.screens[2].ids["welcome_label"].text = f"Welcome, {app.current_user.first} to Geshenk!"
		if page == "make_a_purchase" :
			self.screen_manager.screens[3].ids["nav_drawer"].set_state("close")
			self.animate_subtitle(self.screen_manager.screens[3].ids["make_a_purchase_img"], -.2)
			self.get_menu_data()
		if page == "profile" :
			self.screen_manager.screens[4].ids["nav_drawer"].set_state("close")
			self.animate_subtitle(self.screen_manager.screens[4].ids["profile_img"], -.2)
			self.screen_manager.screens[4].ids["username_label"].text = self.current_user.username
			self.screen_manager.screens[4].ids["first_name_label"].text = self.current_user.first
			self.screen_manager.screens[4].ids["last_name_label"].text = self.current_user.last
			self.screen_manager.screens[4].ids["admin_label"].text = str(self.current_user.admin)
		if page == "overview" :
			self.animate_subtitle(self.screen_manager.screens[5].ids["overview_img"], -.2)
			self.create_purchases_scrlv()

	def animate_subtitle(self, widget, y, *args) :
		animate = Animation(pos_hint={"center_x" : .5, "center_y" : .85}, duration=.01)
		animate += Animation(pos_hint={"center_x" : .5, "center_y" : .76+y}, duration=.5)

		animate.start(widget)

	def animate_failed_login(self, widget, *args) :
		animate = Animation(pos_hint={"center_x" : .5, "center_y" : .27}, duration=.05)

		for i in range(5, 1, -1) :
			animate += Animation(pos_hint={"center_x" : .5+i/100, "center_y" : .27}, duration=.05)
			animate += Animation(pos_hint={"center_x" : .5-i/100, "center_y" : .27}, duration=.05)

		animate += Animation(pos_hint={"center_x" : .5, "center_y" : .27}, duration=.05)

		animate.start(widget)

	def find_user_by_username(self, username) :
		with self.settings.conn :
			self.settings.cur.execute("""
				SELECT * FROM users WHERE username = :username
				""", {"username" : username})

		return self.settings.cur.fetchone()

	def login(self) :
		username_entry = self.screen_manager.screens[1].ids["username_entry"].text
		password_entry = self.screen_manager.screens[1].ids["password_entry"].text

		user = self.find_user_by_username(username_entry)
		if user :
			if bcrypt.checkpw(password_entry.encode("utf-8"), user[1]) :
				self.screen_manager.screens[1].ids["username_entry"].text = ""
				self.screen_manager.screens[1].ids["password_entry"].text = ""

				self.current_user = User(user[0], user[2], user[3], user[4])
				self.change_page("dashboard")
				return True
		
		# print("Not Found!")
		self.screen_manager.screens[1].ids["username_entry"].text = ""
		self.screen_manager.screens[1].ids["password_entry"].text = ""

		self.animate_failed_login(self.screen_manager.screens[1].ids["login_button"])

	def sign_out(self, *args): 
		# if not self.dialog_box :
		self.dialog_box = MDDialog(
			title="Logout Confirmation",
			text = "Are you sure you want to logout?",
			buttons = [
				MDFlatButton(
					text = "No",
					on_release= self.close_dialog),
				MDFlatButton(
					text = "Yes",
					on_release = self.signed_out)])
		self.dialog_box.open()

	def signed_out(self, *args) :
		self.close_dialog()
		self.change_page("login")

	def exit(self, *args): 
		self.dialog_box = MDDialog(
			title="Exit Confirmation",
			text = "Are you sure you want to exit?",
			buttons = [
				MDFlatButton(
					text = "No",
					on_release= self.close_dialog),
				MDFlatButton(
					text = "Yes",
					on_release = self.quit)])
		self.dialog_box.open()

	def quit(self, *args) :
		exit()

	def close_dialog(self, *args) :
		self.dialog_box.dismiss()
		self.root.screens[2].ids["nav_drawer"].set_state("close")
		self.root.screens[3].ids["nav_drawer"].set_state("close")
		self.root.screens[4].ids["nav_drawer"].set_state("close")

	def get_menu_data(self) :
		category_counter = 0
		self.categories = []
		self.menu = {}

		with self.settings.conn :
			self.settings.cur.execute("SELECT * FROM menus ORDER BY category")

		self.menu =  self.settings.cur.fetchall()

		for i in range(len(self.menu)) :
			if not(self.menu[i][2] in self.categories) :
				self.categories.append(self.menu[i][2])

		# self.categories = ["a", "b", "c", "d", "e", "f", "g"]
		counter = len(self.categories)


		for i in range(len(self.categories)) :
			self.screen_manager.screens[3].ids[f"category_frame"].size_hint = (counter/5, 1)
			self.screen_manager.screens[3].ids[f"category_frame"].add_widget(
				Button(
					text 	 = self.categories[i], size_hint=(1/counter,1),
					pos_hint = {"center_x" : ((1/counter*(i+1))-1/counter/2), "center_y" : .5},
					on_press = lambda cat = self.categories[i], *args :self.category_button_clicked(cat),
					color 	 = (1,1,1),
					background_color = (124/255, 49/255, 43/255, 100/255)))

		# 	print((1/counter*(i+1))-1/counter/2)
		# print(self.categories)

	def reset_purchases(self, *args) :
		self.purchase = {}
		try :
			self.screen_manager.screens[3].ids["menu_scrlv"].remove_widget(self.main_layer)
		except :
			pass

	def make_menu_layer(self, item, i, counter) :
		layer = MDFloatLayout(md_bg_color= (230/255-((20/255)*(i%2)), 230/255-((20/255)*(i%2)), 230/255-((20/255)*(i%2)), 1),
							size_hint=(1, 1/counter),
							pos_hint = {"center_x" : 0.5, "center_y" : ((1/counter*(i+1))-1/counter/2)})

		layer.add_widget(MDLabel(text=item,
								halign="left",
								pos_hint = {"center_x" : .52, "center_y" : .5},
								theme_text_color = "Custom",
								text_color = (0,0,0,1),
								font_name = "Barlow",
								font_size = "16sp",
								bold = True))
		layer.add_widget(Button(
							text = "+",
							on_press = lambda *agrs:self.add_button_clicked(item),
							pos_hint = {"center_x" : .7, "center_y" : .5},
							size_hint = (None, None),
							size = (30, 30),
							color 	 = (1,1,1),
							background_color = (100/255, 100/255, 100/255, 1)))

		counter_label = MDLabel(halign="left",
								pos_hint = {"center_x" : 1.29, "center_y" : .5},
								theme_text_color = "Custom",
								text_color = (0,0,0,1),
								font_name = "Barlow",
								font_size = "16sp",
								bold = True)
		try :
			counter_label.text = str(self.purchase[item]["qty"])
		except :
			counter_label.text = "0"

		self.labels.append(counter_label)
		layer.add_widget(counter_label)
		self.items_in_lables.append(item)
		# self.screen_manager.screens[3].ids[f"{item}_counter_label"] = weakref.ref(counter_label)

		layer.add_widget(Button(
							text = "-",
							on_press = lambda *agrs:self.subtract_button_clicked(item),
							pos_hint = {"center_x" : .9, "center_y" : .5},
							size_hint = (None, None),
							size = (30, 30),
							color 	 = (1,1,1),
							background_color = (100/255, 100/255, 100/255, 1)))

		return layer

	def make_purchase_layer(self, item, i, counter, qty, price, total_price) :
		# print(i)
		layer = MDFloatLayout(md_bg_color= (230/255-((20/255)*(i%2)), 230/255-((20/255)*(i%2)), 230/255-((20/255)*(i%2)), 1),
							size_hint=(1, 1/counter),
							pos_hint = {"center_x" : 0.5, "center_y" : ((1/counter*(i+1))-1/counter/2)})

		layer.add_widget(MDLabel(text=str(qty),
								halign="left",
								pos_hint = {"center_x" : .52, "center_y" : .5},
								theme_text_color = "Custom",
								text_color = (0,0,0,1),
								font_name = "Barlow",
								font_size = "16sp",
								bold = True))

		layer.add_widget(MDLabel(text=item,
								halign="left",
								pos_hint = {"center_x" : .58, "center_y" : .5},
								theme_text_color = "Custom",
								text_color = (0,0,0,1),
								font_name = "Barlow",
								font_size = "16sp",
								bold = True))

		layer.add_widget(MDLabel(text=str(price),
								halign="left",
								pos_hint = {"center_x" : 1, "center_y" : .5},
								theme_text_color = "Custom",
								text_color = (0,0,0,1),
								font_name = "Barlow",
								font_size = "16sp",
								bold = True))

		layer.add_widget(MDLabel(text=str(total_price),
								halign="left",
								pos_hint = {"center_x" : 1.3, "center_y" : .5},
								theme_text_color = "Custom",
								text_color = (0,0,0,1),
								font_name = "Barlow",
								font_size = "16sp",
								bold = True))

		return layer

	def category_button_clicked(self, category, *args) :
		try :
			self.screen_manager.screens[3].ids["menu_scrlv"].remove_widget(self.main_layer)
		except :
			pass

		menus = []
		self.layers = []
		
		for item in self.menu :
			if item[2] == category.text :
				menus.append(item)

		self.main_layer = MDFloatLayout(md_bg_color=(0,0,0,1), size_hint=(1,1), pos_hint={"center_x" : .5, "center_y" : .5})
		self.layers = []
		# menus = [(1, "a"),(2, "b"),(3, "c"),(4, "d"),(5, "e"),(6, "f"),]
		counter = len(menus)

		self.main_layer.size_hint = (1, counter/5)
		self.labels = []
		self.items_in_lables = []

		for i in range(counter-1, -1, -1) :
			layer = self.make_menu_layer(menus[i][1], i, counter)

			self.main_layer.add_widget(layer)
			self.layers.append(layer)

		self.screen_manager.screens[3].ids["menu_scrlv"].add_widget(self.main_layer)

	def add_button_clicked(self, item, *args) :
		if not(item in self.purchase) :
			for item2 in self.menu :
				if item2[1] == item :
					price = item2[3]
			items = {
				"qty" : 1,
				"price" : price,
				"total_price" : price,
			}
			self.purchase[item] = items
		else :
			self.purchase[item]["qty"] += 1
			self.purchase[item]["total_price"] +=self.purchase[item]["price"]

		# print(self.purchase)

		self.labels[self.items_in_lables.index(item)].text = str(self.purchase[item]["qty"])

	def subtract_button_clicked(self, item, *args) :
		if (item in self.purchase) :
			if self.purchase[item]["qty"] > 0 :
				self.purchase[item]["qty"] -= 1
				self.purchase[item]["total_price"] -=self.purchase[item]["price"]
			else :
				del self.purchase[item]

		# print(self.purchase)
		try :
			self.labels[self.items_in_lables.index(item)].text = str(self.purchase[item]["qty"])
		except :
			pass

	def create_purchases_scrlv(self) :
		try :
			self.screen_manager.screens[5].ids["purchases_scrlv"].remove_widget(self.main_layer2)
		except :
			pass

		counter = 0
		for key, value in self.purchase.items() :
			counter += 1

		self.main_layer2 = MDFloatLayout(md_bg_color=(0,0,0,1), size_hint=(1,1), pos_hint={"center_x" : .5, "center_y" : .5})
		self.main_layer2.size_hint = (1, counter/5)

		i = 0
		for key, value in self.purchase.items() :
			layer = self.make_purchase_layer(key, i, counter, value["qty"], value["price"], value["total_price"])
			self.main_layer2.add_widget(layer)
			i += 1

		self.screen_manager.screens[5].ids["purchases_scrlv"].add_widget(self.main_layer2)

	def print_button_clicked(self, *args) :
		self.dialog_box = MDDialog(
			title="Print Error",
			text = "Print Function is not available yet. Please wait for further update.",
			buttons = [
				MDFlatButton(
					text = "Ok",
					on_release= self.close_dialog)])
		self.dialog_box.open()


if __name__ == "__main__" :
	app = Geschenk()
	app.run()