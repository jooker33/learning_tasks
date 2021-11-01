
a=[1,1,1,3,3,3,4]

#First case.Extending massive.Deleting excess.
'''
print(a)
print(len(a),'длина до итераций')
for i in range(len(a)-1,-1,-1):
	print(i)
	a.append(a[i])
	print('работа первого массива')
print(a,'- Итог рабты первого цикла')
print(len(a),'длина после итерации')

for k in range(0,len(a)//2):
	print('работа второго массива')
	print(k)
	
	a.remove(a[k])
	print(a)

#Second case. With one extra veriable

'''
'''
b=0
print(a)
for i in range(0,len(a)//2):

	b=a[len(a)-i-1]
		
	a[len(a)-i-1]=a[i]
		
	a[i]=b
	print(a)
		
print(a)

'''


#3rd case/ using corteges

for i in range(0,len(a)//2):
	(a[i],a[len(a)-i-1])=(a[len(a)-i-1],a[i])

print(a)
