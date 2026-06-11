"""--Basic Level (1–7)--"""

"""Write a function to find factorial of a number using recursion."""
# def factorial(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5)) 

"""Write a recursive function to find sum of first n natural numbers."""
# def sum_natural(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum_natural(n-1)
# print(sum_natural(5)) 

"""Print numbers from 1 to n using recursion."""
# def print_number(n):
#     if n == 21:
#         return 1
#     else:
#         print(n,end=" ")
#         return print_number(n+1)

# print_number(1)

"""Print numbers from n to 1 using recursion."""
# def print_number(n):
#     if n==0:
#         return 0
#     else:
#         print(n,end=" ")
#         return print_number(n-1)
# print_number(20)    

"""Find power of a number (a^b) using recursion."""

# def power(a,b):
#     if b==0:
#         return 1
#     else:
#         return a*power(a,b-1)
    
# print(power(2,5))    


# Find GCD of two numbers using recursion.



# Find sum of digits of a number using recursion.
# def sum_digit(n):
#     if n==0:
#         return 0
#     else:
#         return n%10 + sum_digit(n//10)
    
# print(sum_digit(123))    