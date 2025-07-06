# Assignment - 21 Full Stack Web Development using Python MySirG

# Recursion

# 1. Write a recursive python function to print first N natural numbers.

# def natural(n):
#     if n==0:
#         return
#     x=natural(n-1)
#     print(n)
# natural(10)


# 2. Write a recursive python function to print first N natural numbers in reverse order.
# def natrev(n):
#     if n==0:
#         return
#     print(n, end=' ')
#     natrev(n-1)
# natrev(10)



# 3. Write a recursive python function to print first N odd natural numbers.

# 4. Write a recursive python function to print first N odd natural numbers in reverse order

# 5. Write a recursive python function to print first N even natural numbers.


# 6. Write a recursive python function to print first N even natural numbers in reverse
# order.



# 7. Write a recursive python function to print squares of first N natural numbers
# def square(n):
#     if n==0:
#         print("value is",n)
#         exit()
#     square(n-1)
#     print("Square of",n,"=",n**2)
# (square(0))


# 8. Write a recursive python function to print cubes of first N natural numbers
# def cube(n):
#     if n==0:
#         return 0
#     cube(n-1)
#     print("cube of", n,"=",n**3,)
# cube(5)


# 9. Write a recursive python function to print first N multiples of a given number.
def nmultiply(n,a):
    # a=int(input("Enter A number"))
    if n==0:
        return 0
    nmultiply(n-1,a)
    print(a*n, end=' ')
nmultiply(10,7)

# 10.Write a recursive python function to print a number in reverse order.