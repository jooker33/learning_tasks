import random
a=[]
what=0
how_much_list=[]
how_much_in_a_row=2

print('А Максон Сосёт большую бибу!!)')

for i in range(0,10001):
	what=random.randint(0,9)
#	print(i)
	a.append(what)
#print(a)
#print(len(a))


counter=0
for h in range(-1,len(a)-1):

	if a[h]==a[h+1]and h!=len(a):
#		print(a[h],'и его пара',a[h+1])
		for k in range(2,len(a)-2-h):
			if a[h+1]==a[h+k]:
				
				how_much_in_a_row+=1
			else:
				how_much_list.append(how_much_in_a_row)
				how_much_in_a_row=2

				counter+=1
				break
		

how_much_list.sort(reverse=True)
#print(how_much_list)
print(how_much_list[0],'- максимальная длина')
#print(counter,'Пар')