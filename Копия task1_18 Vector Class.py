
class vector():
	def __init__(self,x_coord,y_coord):
		self.x_coord=x_coord
		self.y_coord=y_coord

	def __add__(self,other):
		return vector(self.x_coord + other.x_coord,self.y_coord+other.y_coord)

	def __repr__(self):
		return 'Vector({}, {})'.format(self.x_coord,self.y_coord)

vector_1=vector(1,3)
#Вывели значения координат Х и Y
print(vector_1.x_coord, vector_1.y_coord)
print(vector_1+vector_1)
print(1+2)

