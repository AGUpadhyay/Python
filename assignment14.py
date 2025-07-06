# 1. Write a Python script to create a list of first N natural numbers.
# natural=int(input("Enter value"))
# mylist=[]
# x=1
# while (x<=natural):
#     mylist.append(x)
#     x+=1
# print(mylist)





# 2. Write a Python script to create a list of first N odd natural numbers.

# natural=int(input("Enter value"))
# mylist=[]
# x=1
# a=1
# while (x<=natural):
#     mylist.append(a)
#     a=a+2
#     x+=1
# print(mylist)



# 3. Write a Python script to create a list of first N even natural numbers.

# natural=int(input("Enter value"))
# mylist=[]
# x=1
# a=2
# while (x<=natural):
#     mylist.append(a)
#     a=a+2
#     x+=1
# print(mylist)


# 4. Write a Python script to find the greatest number in a given list of numbers.

# elem=int(input("Enter element in list"))
# x=1
# mylist=[]
# while x<=elem:
#     d=int(input("Enter element of list"))
#     mylist.append(d)
#     x+=1
# print("Max value is",max(mylist), "in mylist", mylist)


# 5. Write a Python script to find the smallest number in a given list of numbers.

# elem=int(input("Enter element in list"))
# x=1
# mylist=[]
# while x<=elem:
#     d=int(input("Enter element of list"))
#     mylist.append(d)
#     x+=1
# print("Min value is",min(mylist), "in mylist", mylist)

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.

# elem=int(input("Enter element in list"))
# x=1
# mylist=[]
# while x<=elem:
#     d=int(input("Enter element of list"))
#     mylist.append(d)
#     x+=1
# print("Sum of list Element is",sum(mylist), "in mylist", mylist)



# 7. Write a Python script to remove all non int values from a list.


# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
# 9. Write a Python script to print indices of all occurrences of a given element in a given list.



# 10. Write a python script to sort a list.

elem=int(input("Enter element in list"))
x=1
mylist=[]
while x<=elem:
    d=int(input("Enter element of list"))
    mylist.append(d)
    x+=1
mylist.sort()
print(mylist)