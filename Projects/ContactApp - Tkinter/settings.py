class Settings :
	def __init__(self) :
		# App Config
		self.title = "Contact Apps V2"

		# Window Config
		base = 60
		ratio = (16,9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+200+100"

		# Image Config
		self.logo = "img/logo2.png"

		# Data Dummy
		self.contacts = [
		{
			"081123456789" :{
			"f_name" : "Anass",
			"l_name" : "Azhasr",
			"address" : "Pasar Kussto",
			"email" : "anasajah@ymailss.com"
			}
		},
		{
			"082123456789" :{
			"f_name" : "Bambang",
			"l_name" : "Triadmodjo",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"083123456789" :{
			"f_name" : "Cindy",
			"l_name" : "Situmorang",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"085123456789" :{
			"f_name" : "Dono",
			"l_name" : "Kasino",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"088123456789" :{
			"f_name" : "Egi",
			"l_name" : "Lubis",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"081123456789" :{
			"f_name" : "Anas",
			"l_name" : "Azhar",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"082123456789" :{
			"f_name" : "Bambang",
			"l_name" : "Triadmodjo",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"083123456789" :{
			"f_name" : "Cindy",
			"l_name" : "Situmorang",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"085123456789" :{
			"f_name" : "Dono",
			"l_name" : "Kasino",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"088123456789" :{
			"f_name" : "Egi",
			"l_name" : "Lubis",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"081123456789" :{
			"f_name" : "Anas",
			"l_name" : "Azhar",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"082123456789" :{
			"f_name" : "Bambang",
			"l_name" : "Triadmodjo",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"083123456789" :{
			"f_name" : "Cindy",
			"l_name" : "Situmorang",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"085123456789" :{
			"f_name" : "Dono",
			"l_name" : "Kasino",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"088123456789" :{
			"f_name" : "Egi",
			"l_name" : "Lubis",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"081123456789" :{
			"f_name" : "Anas",
			"l_name" : "Azhar",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"082123456789" :{
			"f_name" : "Bambang",
			"l_name" : "Triadmodjo",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"083123456789" :{
			"f_name" : "Cindy",
			"l_name" : "Situmorang",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"085123456789" :{
			"f_name" : "Dono",
			"l_name" : "Kasino",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"088123456789" :{
			"f_name" : "Egi",
			"l_name" : "Lubis",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"081123456789" :{
			"f_name" : "Anas",
			"l_name" : "Azhar",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"082123456789" :{
			"f_name" : "Bambang",
			"l_name" : "Triadmodjo",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"083123456789" :{
			"f_name" : "Cindy",
			"l_name" : "Situmorang",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"085123456789" :{
			"f_name" : "Dono",
			"l_name" : "Kasino",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"088123456789" :{
			"f_name" : "Egi",
			"l_name" : "Lubis",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"081123456789" :{
			"f_name" : "Anas",
			"l_name" : "Azhar",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"082123456789" :{
			"f_name" : "Bambang",
			"l_name" : "Triadmodjo",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"083123456789" :{
			"f_name" : "Cindy",
			"l_name" : "Situmorang",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"085123456789" :{
			"f_name" : "Dono",
			"l_name" : "Kasino",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		},
		{
			"088123456789" :{
			"f_name" : "Egi",
			"l_name" : "Lubis",
			"address" : "Pasar Kuto",
			"email" : "anasajah@ymail.com"
			}
		}
		]
