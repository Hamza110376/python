# a = [12,2,45,8,-67,-98,-65]

# for i in range(len(a)):
#     if a[i]>0:
#         print(f"positive integers are {a[i]}")
#     else:
#         print(f"negaative integers are {a[i]}")


# a= [4,5,3,2,6,7]

# sum= 0

# for i in a:
#     sum= sum+i

# print(f"the mean is {sum/len(a)}")


# a= [67,89,52,78,96,2,87]

# largest= a[0]

# for i in a:
#     if i> largest:
#         largest= i

# print(largest)


# a= [67,89,52,78,96,2,87,95]

# largest= a[0]
# sec_laargest= a[0]
# for i in a:
#     if i> largest:
#         sec_laargest= largest
#         largest= i
#     elif i> sec_laargest:
#         sec_laargest=i

# print(largest, sec_laargest)



a= [1,2,3,4,5,6]

for i in range(len(a)-1):
    if a[i]< a[i+1]:
        continue
    else:
        print("array is not sorted")
        break

else:
    print("array is sorted")
