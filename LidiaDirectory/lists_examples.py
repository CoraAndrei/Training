a =[3,1,2,6,5]

#a.sort()
#print(f'Sorted list is : {a}')
#print(f'Length of list a is: {len(a)}')
#print(f'Type of a is: {type(a)}')

a. append(10)
##print(f'New value if list is: {a}')
#a.insert(2,'new parameter')
#print(f'New value if list is: {a}')
#b=['test1','test2','test2']
#a.append(b)
#print(f'New value if list is: {a}')
#print(a[7])


#a.extend(b)
#print(f'New value if list is: {a}')
#print(a[7])

#a.insert(2, 'new parameter')
#print(f'New value if list is: {a}')

print(a[2:])
print (a[1:5:1])

# copiere lista in alta valoare
b=a
print(b)
#b[1] = 'new element'
#print(b)
#print(a) #se modifica val catre care se face referinta

b=a[:]
print(b)
b[1] = 'alt element'
print(b)
print(a)

del b[1]
print(b)
print(a)
print(id(b))
print(id(a))