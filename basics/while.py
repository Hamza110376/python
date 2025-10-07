# a= 0

# while a<= 30:
#     print(a)
#     a= a+1
    

# a= 256
# rev=0
# while a> 0:
#     rev= rev*10+ a%10
#     a= a // 10
    
# print(rev)



# a= int(input("enter aa number"))
# copy = a
# rev=0
# while a> 0:
#     rev= rev*10+ a%10
#     a= a // 10
    
# if copy == rev:
#     print("paliddromic number")
# else:
#     print("not a paladdromic number")



import random

num = random.randint(1,11)



tries = 0

while True:
    guess = int(input("please enter the number between 1-10:- "))
    if num == guess:
        tries +=1
        print(f"you guessed it right in {tries} tries")
        break
    elif num < guess:
        print("go a bit low")
        tries +=1
       
    elif num > guess:
        print("go a bit high")
        tries +=1
       
    else:
        print("sorry you are wrong")
        tries +=1
    if tries>=5:
        print("all tries ended you lost")
        break
       