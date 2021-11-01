my_string = input('Введите свою строку здесь ->')


'''

my_string=dsfg dsf gsdfgdfg
fdsgsdf
sdfgdsfg



a=0
for i in my_string.split(' '):

	a+=1

print(f'{a} - Количество слов в твоей строке ')


print('Исполним вывод каждый элемент строки по индексу списка')



for i in range(0,len(my_string.split())):
	
	print(my_string.split()[i],f'Слово {i+1}')


'''
# А теперь допустим мы не знаем метода split() *В начале пробел *Больше одноо пробела

#Строка разделена только одинарными пробелами
counter=0
number =-1
words=''
new_list=[]
for i in my_string:
	number+1
	words+=i
	print(words)
	if i ==' ':
		
		counter+=1
		new_list+=words
		print(new_list,'А вот расширенный список')
		words=''



print(counter, 'Количество слов в строке')
print(new_list,'- А вот список из этих слов')



