print('          While Loop    ')

print('      EX1       ')

n = 5
while n > 0:  # 0 > 0
    n -= 1  # n = 0-1 = -1
    print(n)  # n = -1

print('      EX2       ')

a = ['andrei', 'srj', 'lidia', 'oana', 'andreea', 'daniel']

while a:
    print(a.pop(-1))

print('      EX3       ')

nex3 = 5
while nex3 > 0:
    nex3 -= 1
    if nex3 == 2:
        break
    print(nex3)
print('Loop Just Ended have a nice day :D:P')

print('      EX4       ')

number = 5
while number > 0:
    number -= 1
    if number == 2:
        continue  # skip 2
    print(number)
print("OMG It hase ended finally")

print('      EX5      ')

number = 5
while number > 0:
    number -= 1
    print(f'My value is :{number}')
else:
    print("Looop Is Over Go outside and play now")

print('      EX6      ')

n = 5
while n > 0:
    n -= 1
    print(f'My value is :{n}')
    if n == 2:
        break
else:
    print('Its Over Byeeeeeeee')

print('      EX7      ')

klass = ['Oana', 'Andreea', 'Lidia', 'Daniel', 'SRJ', 'Andrei P.']
is_in_class = 'Lidia'

i = 0
while i < len(klass):
    if klass[i] == is_in_class:
        # Ittem wass fond in Klass
        break
    i += 1
else:
    # Ittem not found in Klass
    print(is_in_class, 'He should be pinked out, he is not in Klass :(.')

print('      EX7.1      ')

if is_in_class in klass:
    print(is_in_class, 'He/She is in class yeeey party mode on :)) .')
else:
    print(is_in_class, 'He should be pinked out, he is not in Klass :(.')

print('      EX8     ')

while True:
    print('Andrei P. vrea un Loop Infinit .....')

print('      EX9      ')

klass = ['Oana', 'Andreea', 'Lidia', 'Daniel', 'SRJ', 'Andrei P.']
while True:
    if not klass:
        break
    print(klass.pop(-1))

print('EX10')

age = 65
gender = 'F'

if age < 18:
    if gender == 'M':
        print('Son')
    else:
        print('Daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('Father')
    else:
        print('Mother')
else:
    if gender == 'M':
        print('Grandfather')
    else:
        print('Grandmother')

print('EX11')

klass = ['Oana', 'Andreea', 'Lidia', 'Daniel', 'SRJ', 'Andrei P.']

while len(klass):
    print(klass.pop(0))
    klass_is_not_paying_attention = ['Gogo', 'Andrei C.']
    while len(klass_is_not_paying_attention):
        print('$$$>>>', klass_is_not_paying_attention.pop(1))

print('EX12')

numbers_of_people_in_class = 7
while numbers_of_people_in_class > 0: numbers_of_people_in_class -= 1; print(numbers_of_people_in_class)

print('EX12.1')

if True: print('All People are in class')

while True:
    print('Andrei P. vrea un Loop Infinit .....')
