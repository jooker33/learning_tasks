class Restaurant():
	def __init__(self,restaurant, cuisine_type):
		self.restaurant=restaurant
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print (f"{self.restaurant} - Название")
		print (f"{self.cuisine_type} - Описание")

	def open_restaurant(self):
		print ('Restaurant is OPEN')


rest_1=Restaurant('Мишлен','5 звёзд')
rest_2=Restaurant('Прага','4 звёзды')
rest_3=Restaurant('Шашлындос','3 звёзды')


rest_1.describe_restaurant()
print(rest_1.restaurant)
print(rest_1.cuisine_type)
rest_1.describe_restaurant()
rest_1.open_restaurant()

rest_2.describe_restaurant()
rest_3.describe_restaurant()



class User():
	def __init__(self, first_name,last_name,male,vk_id):
		self.vk_id=vk_id
		self.first_name=first_name
		self.last_name=last_name
		self.male=male

	def describe_user(self):
		print (self.first_name)
		print (self.last_name)
		print (self.male)
		print (self.vk_id)
	def greet_user(self):
		print (f'Привет, крошка {self.first_name}, ты великолепен!!')


user_1=User('NIkita','Novikov','Muzh','vk.com/novikovnikita')
user_2=User('Erica','Xavier','Jen','vk.com/africacoma')

user_2.greet_user()
user_2.describe_user()
