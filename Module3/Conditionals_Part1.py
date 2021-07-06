print("Start Foo Barr $$$")
#Ex1
# if 'bar' in['bar','air','quiz']:
#     print('I am part of the group')
#     print('or am I?')
# print('Is this really who i am')
#
# print("End Foo Bar $$")

#Ex2
#
# print("Start Does this line execute")
#
# if 'foo' in ['foo','air','tesla']:
#     print("Outer condition is True")
#     if 10>20:
#          print('Inner contition')
#     print('Between Inner Condition')
#
#     if 10<20:
#         print("Inner Condition")
#     print("End of Outer Condition")
# print("After Condition")

#Ex3 if-else

# x=20
#
# if x > 50:
#     print("x is smaller then 50 first condition")
# else:
#     print("x is larger then life")

#Ex4
# name = 'Lidia'
# if name == 'Andreea':
#     print("Hello Andreea and be Well")
# elif name == 'Lidia':
#     print("Hello Lidia and be Well")
# elif name =='Andrei':
#      print("Hello Andrei and be Well")
# elif name =='Sergiu':
#     print("Hello Sergiu and be Well")
# elif name == 'Daniel':
#     print("Hello Daniel and be Well")
# else:
#     print(f"I do not know who you are *** {name} ***")

# Ex5 dictionar de names

# names = {'Andreea':'Hello Andreea',
#          'Lidia':'Hello Lidia',
#          'Andrei':'Hello Andrei',
#          'Sergiu':'Hello Sergiu',
#          'Daniel':'Hello Daniel',
#          'Gogo':'Hello Gogo'
#          }
# print(names.get('Lidia'),f'Do I know or do I?who you are')
#
# new_name = 'Gogo'
# print(names.get(new_name), f'Do you know who I am? I/m not in this class {new_name} ')

#Ex6

# class_pres = 1
#
# if class_pres ==1:
#
#     print('Andrei');print('Andreea');print('Andrei P')
# elif class_pres == 2:
#     print('Lidia'); print('Daniel'); print('Sergiu')
#
# elif class_pres ==3:
#     print('Gogo');print('Cora')
# elif class_pres == 4:
#     print('Yeyy');print('Everyoane is in class')
# else:
#     print("Really no one is in the class V?")
# print('####')
#
# if 'Gogo' in 'Gogo is present in this class': print('yes');print('who knows')
# print('Andrei C') if class_pres == 7 else print('Andrei is not in class')

#Ex7

# monthly_income = 100  # $100
# monthly_expenses = 500  # $500
# print("You are in the Green go ahead..... ") if monthly_income> monthly_expenses else print('=')\
#       if monthly_income == monthly_expenses else print('Stop it')
#



#Ex8
# monthly_expenses = 200
# fun_expenses = 33
# monthly_income = 500
# rem_bug = monthly_income-monthly_expenses-fun_expenses
#
# if monthly_expenses> fun_expenses  or  monthly_income>monthly_expenses:
#     print(f"You are in the Green")
# else:
#     print('Stop it')