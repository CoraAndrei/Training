# Ex1
print("Exercise1")
nota = 5
if nota > 5:
    print(f"Ai trecut examenul cu nota {nota} ")
elif nota < 5:
    print(f"Nu ai trecut examenul, nota obtinuta este {nota}")
else:
    print("Data viitoare sa te pregatesti mai bine")

# 2. Write if statement to check if a person is over the age of 18 or not. print out the the age and a message.
print("Exercise2")
age = 100
if age > 18:
    print(f"Esti major/a, ai {age} ani ")
if age < 18:
    print(f"Esti minora, ai {age} ani")

# 3 Compare what number is greater between a , b and c (Hint: this exercise will need if ,
# elif, else, and , < , > )
print("Exercise3")
a = 10
b = 15
c = 30

if a >= b and a>=c:
   print(f'The greater number is {a}')
elif b>=a and b>=c:
   print(f'The greater number is {b}')
else:
   print(f'The greater number is {c}')


# 4. Define a dictionary with at least 6 key value pairs and print the first the 1 the 2 and the 6 values from the dict.
print("Exercise4")

qa_team = {'Andrei': 5,
           'Daniel': 4,
           'Sergiu': 3,
           'Andreea': 2,
           'Lidia': 1,
           'Florina': 5,
           'Gogo': 9}
print("The values are: ", qa_team.get('Daniel'), qa_team.get('Sergiu'), qa_team.get('Gogo'))

# 5. Check if a number is odd or even and print if the number is even or odd.( Hint %2==0)
print("Exercise5")

case_1_num = 65443
case_2_num = 6542
if (case_1_num % 2) == 0:
    print(f"{case_1_num} is even")
elif(case_2_num % 2) == 0:
    print(f"{case_2_num} is even")
else:
  print("Another message...")



