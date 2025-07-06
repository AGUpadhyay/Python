# Assignment - 22 Full Stack Web Development using Python MySirG
# More on Recursion

# 1. Write a recursive python function to calculate sum of first N natural numbers.

# def nsum(n):
#     if n==0:
#         return 0
#     return n+nsum(n-1)
# a=int(input("Enter a value"))
# b=nsum(a)
# print("Value is", b)

# 2. Write a recursive python function to calculate sum of first N odd natural numbers

# 3. Write a recursive python function to calculate sum of first N even natural numbers
# 4. Write a recursive python function to calculate sum of squares of first N natural
#    numbers

def nsq(n):
    if n==0:
        return 0
    return n**2+nsq(n-1)
a=int(input("Enter Value\t"))
b=nsq(a)
print("Sum of squares of first N Natural Number is =",b,"and N is =",a)

# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers
# 6. Write a recursive python function to calculate the factorial of a number.
# 7. Write a recursive python function to calculate sum of the digits of a given number
# 8. Write a recursive python function to print binary of a given decimal number.
# 9. Write a recursive python function to print octal of a given decimal number
# 10. Write a recursive python function to find the Nth term of the Fibonacci series.