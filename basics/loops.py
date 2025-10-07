# for loop

# a= range(1,20)

# for i in a:
#     print(i)


# reverse loop

# a= range(20,0,-1)

# for i in a:
#     print(i)


# printing a table

# a=range(5,51,5)

# for i in a:
#     print(i)


# taking an input to print aaa table

# n= int(input("please input a number: "))

# for i in range(n, (n*10)+1,n ):
#     print(f"{n*n}={i}")



# for loop on strings

# a= "Hamza is the real boss"

# for i in range(len(a)):
#     print(a[i])


# if else break ccontinue in a for loop

# for i  in range(1,23):
#     if i==16:
#         print("break statement executed")
#         break
#     print(i)
# else:
#     print("break statement is not executed")

# for i  in range(1,23):
#     if i==16:
#         print("break statement executed")
#         continue
#     print(i)
# else:
#     print("break statement is not executed")

# Q1

# n= int(input("enter a number "))

# for i in range(n):
#     print("hello world")


# q2

# n= int(input("enter aa number: "))

# for i in range(0,n):
#     print(i)


# q3

# n= int(input("enter aa number: "))
# for i in range(n,0,-1):
#     print(i)

# Q4
# n= int(input("enter aa number: "))

# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")


# q5

# n= int(input("enter a number: "))
# sum=0
# for i in range(1,(n+1)):
#    sum= sum+i

# print(sum)


# Q6

# n= int(input("enter a number: "))
# fact=1
# for i in range(1,(n+1)):
#    fact= fact*i

# print(fact)

# Q7

# n= int(input("enter a number: "))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
       
#     else:
#         odd=odd+i
# print(f"{even,{odd}}")       

# Q8

# n= int(input("enter a number: "))

# for i in range(1,n+1):
#     if n%i ==0:
#         print(i)

# Q9
# n= int(input("enter a number: "))
# sum= 0

# for i in range(1, n):
   
#     if n%i ==0 :
#        sum= sum+i

# if sum == n:
#     print("number is perfect")

# else:
#     print("number is not perfect")

# Q10

# n= int(input("enter a number: "))
# count=0
# for i in range(1,n+1):
#     if n%i ==0:
#         count= count+1

# if count ==2:
#     print("number is primary")
# else:
#      print("number is not primary")

# q11
# name = "hamza"

# b=""
# for i in range(len(name)-1,-1,-1):
#     b=b+name[i]
#     print(b)
# if b == name:
#     print("word is palindrome")
# else:
#     print("word is not palindrome")

# q12

n="deudheude$%^&@@!#$7378823289398"

string=0
dig=0
spclchar=0

for i in n:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        string += 1
    else:
        spclchar += 1

print(f"count of special character are {spclchar} count of digits are {dig} count of aalp[habet are {string}]")






       
