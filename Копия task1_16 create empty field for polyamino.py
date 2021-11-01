def fill_start_coordinates(a):
	
	#a - 'элемент списка, описывающий 1 полиомино'
	#Присвоим каждой клетке прямогульного полиомино свои координату начального положения, которые будут меняться при сдвиге фигуры относительно начального состояния
	#Пускай список ХУ содержит списки пар исходных координат
	#Сетка координат начнётся с 1,1
	XY = [[i,j] for i in range (1,a[0][0][0]+1) for j in range(1,a[0][0][1]+1)]
	
if __name__ == '__main__':
	M=int(input('Введите ширину поля -  ')) #Width
	N=int(input('Введите высоту поля-  ')) #Height
	
	print('Введите параметры прямоугольных полиомино, а также мощность, каждого из подмножеств',end='\n'*2)
	
	print('Введите параметры i-го прямоугольного полиомино(Для прекращения ввода введите любую букву):')
	i=0
	k=0
	Power_1=0
	Mnozestvo_priyam_pol= []
	while (i or k or Power_1)!='stop':
		try: 							
			i=int(input('Ширина -  '))
			k=int(input('Высота -  '))
			Power_1=int(input('Введите мощность данного подмножества -  '))
			print(f'Вы задали {Power_1} прямоугольных полиомино с параметрами [({i},{k})]')
		except ValueError:
			print('Работа с вводом завершена. Переход к след шагу ....')
			break
		
		
		Mnozestvo_priyam_pol+=[[(i,k),Power_1]]
	
	print('Вы задали след. множество P - полимино -  ',Mnozestvo_priyam_pol,end='\n'*2)
	
	
	print('Введите параметры L-угольных полиомино, а также мощность, каждого из подмножеств',end='\n'*2)
	
	print('Введите параметры i-го L-угольного полиомино (Для прекращения ввода введите любую букву):')
	i=0
	k=0
	Power_1=0
	Mnozestvo_Lug_pol= []
	while (i or k or Power_1)!='stop':
		try: 							
			i=int(input('Ширина -  '))
			k=int(input('Высота -  '))
			Power_1=int(input('Введите мощность данного подмножества -  '))
			print(f'Вы задали {Power_1} прямоугольных полиомино с параметрами [({i},{k})]')
		except ValueError:
			print('Работа с вводом завершена. Переход к след шагу ....')
			break
			
		
		Mnozestvo_Lug_pol+=[[(i,k),Power_1]]
	
	print('Вы задали след. множество L - полимино -  ', Mnozestvo_Lug_pol,end='\n'*2)
	
	
	#Create a tuple matrix of a field M*N size
	Tuple_matrix=[]
	for i in range(0,M+1):
		for k in range(0,N+1):
			Tuple_matrix+=[(i,k)]# All coordinates on a field
	
	print('Координаты клеток стола Т -  ',Tuple_matrix)
	
	
	
			
	fill_start_coordinates(Mnozestvo_priyam_pol)
	
	#Листы с полиомино и матрица поля готовы. Осталось посчитать количество всех возможных комбинаций каждого полиомино на поле.
