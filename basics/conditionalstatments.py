# Q1

# number1= int(input('enter the number 1: '))
# number2= int(input('enter the number 2: '))

# if number1>number2:
#     print('Number1 is greater')
# else:
#         print('Number2 is greater')


# Q2

# gender = str(input('what is your gender: '))

# if gender == "male":
#       print("Good morning sir!")

# elif gender == "female":
#       print("Good morning mam!") 



# Q3

# number = int(input("Please enter a number: "))

# if number%2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# Q4

# name= str(input("please enter your name: "))
# age = int(input("please enter your age: "))

# if age>=18:
#     print(f"{name} is eligible for voting")
# else:
#     print(f'{name} is not eligible for voting')


# Q5

# year = int(input("enter the year: "))

# if year%4 ==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# Q6

temperature= int(input("Enter the temperature: "))

if temperature< 0:
    print("freezing cold")
elif temperature>=0 and temperature<=10:
    print("Very cold")
elif temperature>10 and temperature<=20:
    print("cold")
elif temperature>20 and temperature<=30:
    print("Pleasant")
elif temperature>30 and temperature<=40:
    print("Hot")
elif temperature>40:
    print("very hot")