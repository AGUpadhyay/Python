# 1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list

# mylist=["Java", "Python", "SQL", "C"]
# print(mylist)


# 2. Write a python script to get the data type of a list.

# mylist=["Java", "Python", "SQL", "C"]
# print(type(mylist))


# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

# mylist=["Java", "C", "Python"]
# print(mylist[-1])

# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

# mylist=["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
# mylist[1]="SQL"
# mylist[3]="Reactnative"                      #------------------------------------------------------------->Editing a list
# print(mylist)


# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]

# mylist=["Java", "SQL", "C", "Reactnative"]
# mylist.append("Python")
# print(mylist)

# 6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )


# firstlist, secondlist = ["Java", "Python", "SQL"],["C", "Cpp", "NoSQL"]
# for x in secondlist:
#     firstlist.append(x)
# print(firstlist)

# 7. Write a python program to Print all items by referring to their index number (thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# i=0
# while (i<len(thislist)):
#     print(thislist[i], end= ' ')
#     i=i+1


# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
# thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
# thislist.sort()
# print(thislist)



# 9. Write a Python script to create a list of city names taken from the user.

elem=int(input("Enter Number of City"))
x=1
mylist=[]
while x<=elem:
    d=str(input("Enter City Name"))
    mylist.append(d)
    x+=1
print(mylist)

# 10. Write a Python script to create a list, where each element of the list is a digit of agiven number.
# a=input("Enter a number")
# print(list(a))