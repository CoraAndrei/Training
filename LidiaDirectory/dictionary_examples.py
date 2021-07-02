# a= {'key': 'value'}

a= {'first_key' : 3}

print(f'Dict has a value: {a}')
print(f'Dict has a value: {a.keys()}')
print(f'Dict has a value: {a.values()}')
print(type(a))

#creare cheie noua

a['new_key'] =5
print(f'Dict has a value: {a}')
print(f'Dict has a value: {a.keys()}')
print(f'Dict has a value: {a.values()}')

#adaugare
a['third_key'] = [1,2,3]
print('\n')
print(f'Dict has a value: {a}')
print(f'Dict has a value: {a.keys()}')
print(f'Dict has a value: {a.values()}')

#modificare
a[1]=2
print(f'Dict has a value: {a}')
a['new_key']= 10
print('\n')
print(f'Dict has a value: {a}')
print(f'Dict has a value: {a.keys()}')
print(f'Dict has a value: {a.values()}')

#stergere cheie

del a['new_key']

print('\n')
print(f'Dict has a value: {a}')
print(f'Dict has a value: {a.keys()}')
print(f'Dict has a value: {a.values()}')