a = [7, 2, 3, 4, 5]

a.sort()
print (f'value of list is: {a}')


print (f'Length of list is: {len(a)}')

a.append(10)
print (f'value of list is: {a}')

a.insert(2, 'new paramenter')
print (f'value of list is: {a}')

b = ['test1', 'test2', 'test3']

a.append(b)
print (f'value of list is: {a}')

a.extend(b)
print (f'value of list is: {a}')
