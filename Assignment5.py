# 1. Write a python script to remove the last digit from a given number. (for example, if
#    user enters 2534 then your output should be 253)

# a=int(input("Enter A Number\t"))
# a=a//10
# print(a)



# 2. Write a python script to get the last digit from a given number. (for example, if user
#    enters 2089 then your output should be 9)

# a=int(input("Enter A Number\t"))
# a=a%10
# print(a)




# 3. Write a python script to swap data of two variables

# a,b= int(input("Enter a Number\t")), int(input("Enter a Number\t"))
# c=b
# b=a
# a=c
# print("Swapped! a = ",a,"b = ",b)



# 4. Write a python script to find x power y, where values of x and y are given by user

# x,y = int(input("Enter value of X")), int(input("Enter value of Y"))
# x=x**y
# print(x)





# 5. Write a python script which takes a three digit number from the user and displays
#    only its first digit.

# a=int(input("Enter three digit Number"))
# a=a//100
# print(a)




# 6. Write a python script which takes a three digit number from the user and displays
#    only its middle digit.

# a=int(input("Enter three digit Number"))
# a=a//10
# a=a%10
# print(a)



# 7. Write a python script which takes a three digit number from the user and displays
#    only its last digit.

# a=int(input("Enter three digit number\t"))
# a=a%10
# print(a)




# 8. Write a python script to use IN operator to display the data present in the list

# a=[1,2,3,4,5,6,7,8,9,10]
# for x in a:
#     print(x)





# 9. Write a python script to use NOT IN operator to display the data not present in list

# a= [1,2,3,4,5,6,7]
# b=[2,5,8]
# for x in a:
#     if x not in b: #----------------------------------- TO COMPARE TWO LISTS ELEMENT
#         print(x)



# 10. Write a python script to use IS operator to display if both variables are the same
#     object or not?

a,b= int(input("Enter any number")), int(input("Enter any number"))
if a is b:
    print(id(a),"and", id(b))
else:
    print("Not Equal")