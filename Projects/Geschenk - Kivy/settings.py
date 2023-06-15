import sqlite3

class Settings :
	conn = sqlite3.connect("data/geschenk.db")
	cur = conn.cursor()