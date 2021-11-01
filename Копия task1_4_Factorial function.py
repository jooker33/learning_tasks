
import math
# Факториал
def factorio_calculatus(num):
	x=1
	for i in range(1,num+1):
		x=x*i
	return(x)
#Определили квадратный корень по приколу
def sqrt(var):
	return(var**(1/2))	

#Попробуем по приколу также определить число пи

def pi():
	result2=0
	for g in range(1,10000):
		
		result2+=(4/(2*g-1))*((-1)**(g+1))
		
	return(result2)	

#Синус с помощью ряда sinx= x-x^3/3!+x^5/5!

def row_sin_calculation(angle):
	result1=0
	
	for k in range(1,50):
		
		result1+=((-1)**(k+1)*(angle**(2*k-1)))/(factorio_calculatus(2*k-1))
		
		

	return (result1)

print(row_sin_calculation(pi()/2))
print(pi())