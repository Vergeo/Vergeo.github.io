import bcrypt
import sqlite3
from getpass import getpass

from settings import Settings
from models.user import User

def main() :
	settings = Settings()
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS users (
			username TEXT PRIMARY KEY,
			password TEXT NOT NULL,
			first TEXT NOT NULL,
			last TEXT NOT NULL,
			admin BOOL NOT NULL
		)
		""")
	settings.cur.execute("SELECT * FROM users WHERE username = 'admin'")
	user = settings.cur.fetchone()

	if not user :
		admin = User(username="admin", first="super", last="admin", admin=True)
		password = getpass("Input New Password for Admin\nPassword : ")
		retype_password = getpass("Retype Password : ")
		attemps = 0
		while retype_password != password :
			if attemps == 3 :
				print("Limit exceeded, please try again!")
				break
			print("Password doesn't match")
			attemps += 1
			retype_password = getpass("Retype Password : ")
		else :
			admin.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			settings.cur.execute("""
				INSERT INTO users (username, password, first, last, admin)
				VALUES (:username, :password, :first, :last, :admin)
				""", {
				"username" : admin.username,
				"password" : admin.password,
				"first" : admin.first,
				"last" : admin.last,
				"admin" : True
				})
			settings.conn.commit()
			print("Super Admin has been created successfully.")

	else :
		print("Admin already exists.")


def create_menu() :
	settings = Settings()
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS menus(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT not null,
		category TEXT not null,
		price INTEGER not null)
		""")

def create_purchases() :
	settings = Settings()
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS purchases(
		history_id INTEGER NOT NULL,
		menu_id INTEGER NOT NULL,
		qty INTEGER NOT NULL,
		total_price INTEGER NOT NULL,
		FOREIGN KEY (history_id) REFERENCES purchase_history (id)
		FOREIGN KEY (menu_id) REFERENCES menus (id)
		)
		""")

def create_purchase_history() :
	settings = Settings()
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS purchase_history(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL DEFAULT "NoName",
		total_price INTEGER NOT NULL DEFAULT 0
		)
		""")


if __name__ == '__main__':
	main()
	create_menu()
	create_purchases()
	create_purchase_history()