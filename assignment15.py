# 1. Write a python script to create a String in 3 different possible ways
# a="Mystring"
# b=str("mystr")
# c='mystring'
# print(type(b), type(a),type(c))

# 2. Write a python script to Get the characters from the start to position 5 (Given String“iNeuron” using the slice syntax)

# s="iNeuron"
# print(s[:5:1])

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String“Hello Learners” using the slice syntax)

# s= "Hello Learners"
# print(s[2:6:1])
# print(s)

# 4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
# a="Learning"
# b="Python"
# c=' '
# print(a+c+b)

# 5. Write a python script to get the count of total number of characters in String a=“iNeuron”
# a= "iNeuron"
# print(len(a))
# 6. Write a python script to reverse a String. (“iNeuron”)

# 5. Write a python script to get the count of total number of characters in String a=“iNeuron”
# a= "iNeuron"
# print(a[::-1])

# 7. Write a python script to determine whether a string contains a specific substring.

# a="iNeuron"
# b="nr"
# if b in a:
#     print("Substring")
# else:
#     print("Not a Substring")


# 8. Write a python script to check if a string contains only numbers.

# a=input("Enter any string")
# print(a.isdigit())


# if a in '0123456789':
#     print("Only numbers")
# else:
#     print("Others are available")



# 9. Write a python script to check if a string contains only characters of the alphabet.

# a=input("Enter any string")
# print(a.isalpha())


# 10. Write a python script to convert an integer to a string.
integer=int(input("Enter a value"))
s=str(integer)
print(type(s))