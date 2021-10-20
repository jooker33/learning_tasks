def check_me_fast(num):
	N=0
	if num%5==0 and num>0:
		N=num//5
		return str(True)+ f' Представление :{N}*5'
	last_character=num%10

	if (last_character==3 or last_character==8) and 3**1<=num:
		N=(num - 3**1)//5
		return str(True)+ f' Представление :3^1 + {N}*5'

	elif (last_character==4 or last_character==9) and 3**2<=num:
		N=(num - 3**2)//5
		return str(True)+ f' Представление :3^2 + {N}*5'

	elif (last_character==2 or last_character==7) and 3**3<=num:
		N=(num - 3**3)//5
		return str(True)+ f' Представление :3^3 + {N}*5'

	elif (last_character==1 or last_character==6) and 3**4<=num:
		N=(num - 3**4)//5
		return str(True)+ f' Представление :3^4 + {N}*5'

	else:
		return str(False)+ f' Представления Нет'



i=True
while i==True:
	print(check_me_fast(int(input())))