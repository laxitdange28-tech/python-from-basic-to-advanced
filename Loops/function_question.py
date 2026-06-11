"""----------Basic Level (1–15)-----------"""

"""Write a function to print "Hello World"."""

# def hello():
#     print("Hello world")

# hello()    

"""Create a function to print your name."""

# def name(name):
#     print(f"Your name is {name}")

# name("Laxit")    

"""Write a function that takes a number and prints it."""

# def number(num):
#     print(num)

# number(5)

"""Create a function to add two numbers."""

# def add(a,b):
#     print(f"Sum of two number = {a + b}")

# num1 = int(input("Enter your 1st number :- "))
# num2 = int(input("Enter your 2nd number :- "))
# add(num1,num2)    

"""Write a function to subtract two numbers."""

# def subtract(a,b):
#     print(f"subtrection of two number {a} - {b} = {a - b}")

# subtract(12,6)    

"""Create a function to multiply two numbers."""

# def multiply(a,b):
#     print(f"Multiplicaton of a two number {a} x {b} = {a*b}")

# multiply(12,5)    

"""Write a function to divide two numbers."""

# def divide(a,b):
#     print(f"Division of two number {a} / {b} = {a//b}")

# divide(12,6)

"""Create a function to check if a number is even or odd."""

# def check_even_odd(number):
#     if number % 2==0:
#         print("Number is even ")
#     else:
#         print("Number is odd ")

# n = int(input("Enter your number to check odd or even :- "))
# check_even_odd(n)          
  
"""Write a function to find the square of a number."""

# def squre(number):
#     print(f"Squre of number {number} = {number **2}")

# n = int(input("Enter your number to find squre :- "))
# squre(n)    

"""Create a function to find the cube of a number."""

# def cube(number):
#     print(f"Cube of a number {number} = {number **3}")

# n= int(input("Enter your number to find cube :- "))
# cube(n)

"""Write a function to print numbers from 1 to 10."""

# def print_number(start,end):
#     for i in range(start,end+1):
#         print(i,end=" ")

# start_point = int(input("Enter a number of start point :- "))
# end_point =  int(input("Enter a number to stop :- "))

# print_number(start_point,end_point)


"""Create a function to print numbers from n to 1."""

"""Write a function to print the table of a number."""

# def table(number):
#     for i in range(1,11):
#         print(f"{number} x {i} = {number*i}")

# n = int(input("Enter your number to find table :- "))
# table(n)

# Create a function to find the maximum of two numbers.

# def maximum(a,b):
#     if a>b:
#         print(f"Maximum number is A = {a}")
#     else:
#         print(f"Maximum number is B = {b}")
# a = int(input("Enter a first number :- "))
# b = int(input("Enter secode number :- "))
# maximum(a,b)            

"""Write a function to find the minimum of two numbers"""
# def minimum(a,b):
#     if a<b:
#         print(f"Minimum number is A : {a} ")
#     else:
#         print(f"Minimum number is B : {b}")

# a ,b = map(int , input("Enter two number :- ").split())

# minimum(a,b)

"""----------------Intermediate Level (16–30)--------------"""

"""Write a function to find the factorial of a number."""

# def factorial(number):
#     fact = 1
#     for i in range(1,number+1):
#         fact *=i
#     print(f"Number {number} factorial is = {fact}")    

# n = int(input("Enter a number to find factorial :- "))
# factorial(n)

"""Create a function to check if a number is prime."""

# def prime(n):
#     for i in range(2,(n//2)+1):
#         if n % i == 0 :
#             print("Number is not prime")
#             break
#     else:
#         print("Number is  prime ")

# num = int(input("Enter a number to check nuber is prime or not :-  "))
# prime(num)

"""Write a function to find the sum of first n natural numbers."""

# def sum_of_natural(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum +=i
#     print(f"Sum of natural number :- {sum}")    

# n = int(input("Enter a n number to faind sum :- "))
# sum_of_natural(n)
        
"""Create a function to find the sum of digits of a number."""
# def sum_digit(n):
#     temp = n
#     sumdigit = 0
#     while temp>0:
#         last_digit = temp % 10
#         sumdigit += last_digit
#         temp //=10

#     print(f"Sum of digit = {sumdigit}")  

# n = int(input("Enter a digit to print sum :- "))
# sum_digit(n)

"""Write a function to reverse a number"""

# def reverse_number(n):
#     rev = 0
#     while n>0:
#         rev = rev*10 + n%10
#         n//=10
#     print(f"Reversr number :- {rev}")   

# n = int(input("Enter a number :- "))
# reverse_number(n)


"""Create a function to check if a number is palindrome."""
# def palindrome(n):
#     temp = n
#     rev = 0
#     while temp>0:
#         rev = rev*10 + temp%10
#         temp //=10
#     if rev==n:
#         print("Number is palindrome")    
#     else:
#         print("Number is Not palindrome")    

# n = int(input("Enter a number to check number is palindrome or not :- "))        
# palindrome(n)

"""Write a function to count digits in a number."""
# method 1
# def count_digit(n):
#     count = 0
#     while n>0:
#         last_digit = n%10
#         count +=1
#         n//=10
#     print(f"Count of digit = {count}")    

# n = int(input("Enter a digit to count :- "))   
# count_digit(n) 

'''Method 2'''
# def count_digit(n):
#     n = str(n)
#     count = len(n)
#     n = int(n)
#     print(f"Count of digit : - {count}")

# n = int(input("Enter a digit to count :- "))   
# count_digit(n) 

"""Create a function to find the largest of three numbers."""
# def largest(a,b,c):
#     if a>b and a>c:
#         print(f"A is a largest number = {a}")
#     elif b>c:
#         print(f"B is la largest number = {b} ")   
#     else:
#         print(f"C is a largest number = {c} ")    

# a,b,c = map(int,input("Enter a three number :- ").split())
# largest(a,b,c)

"""Write a function to print Fibonacci series up to n terms."""
"""Method 1 """
# def fibonacci_series(n):
#     a=0
#     b=1
#     for i in range(1,n+1):
#         c = a+b
#         print(a,end=" ")
#         a=b
#         b=c
# n = int(input("Enter a number to print :- "))
# fibonacci_series(n)  

"""method 2"""
# def fibonacci_series(n):
#     a=0
#     b=1
#     for i in range(1,n+1):
#         print(a, end=" ")
#         a,b = b , a+b      

# n = int(input("Enter a number to print :- "))
# fibonacci_series(n)  

"""Create a function to find GCD of two numbers."""
"""Method 1"""
# def gcd(a,b):
#     small = min(a,b)
#     for i in range(small,0,-1):
#        if a % i ==0 and b % i ==0:
#             return i
# num1 , num2 = map(int,input("Enter two number :- ").split())
# print("GCD = ", gcd(num1,num2))  #GCD(12, 18) = 6

"""Method 2 """
# def gcd(a,b):
#     while b !=0:
#         a , b = b , a%b
#     return a
    
# num1 , num2 = map(int,input("Enter two number :- ").split())   
# print("GCD= ", gcd(num1,num2)) 

"""Write a function to find LCM of two numbers. """
# def lcm(a,b):
#     max_value = max(a,b)
#     while True:
#         if max_value % a ==0 and max_value % b == 0:
#             return max_value
#         max_value +=1

# num1 , num2 = map(int,input("Enter two number :- ").split())   
# print("lcm = ", lcm(num1,num2)) 

"""Create a function to check if a year is a leap year."""
# def leap_year(year):
#     if (year % 4 ==0 and year% 100 !=0) or year % 400 ==0:
#         print("Year is leap year ")
#     else:
#         print("Not a leap year 😌")

# year = int(input("Enter a year :- "))    
# leap_year(year)

"""Write a function to calculate power (x^y)."""
# def calculate_power(a,b):
#     return a**b

# a ,b = map(int,input("Enter a 1st number and power of 1st number :- ").split())
# print("Clculate power = ",calculate_power(a,b))

""""Create a function to print all even numbers up to n."""
# def even_number(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i , end=" ")

# n = int(input("Enter a n  number  to print even number :- "))
# even_number(n)

"""Write a function to print all odd numbers up to n."""
# def odd_number(n):
#     for i in range(1,n+1):
#         if i%2!=0:
#             print(i , end=" ")

# n = int(input("Enter a n number to print even number :- "))
# odd_number(n)

""" Ask the user to enter a number and print all prime numbers up to that number.
Input: 10
Output: 2 3 5 7"""

# def prime_number(n):
#     for i in range(2,n+1):
#         is_prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 is_prime = False
#                 break

#         if is_prime:  
#             print(i,end=" ")


# n = int(input("Enter a range :- "))
# prime_number(n)   

# def print_primes(n):
#     for i in range(2,n+1):
#         a = i
#         for j in range(2,(a//2)+1):
#             if a%j==0:
#                 break
#         else:
#             print(i)    

# n = int(input("inter a  range of number :-  "))
# print_primes(n)   

"""🟠------- String-Based Functions (31–40)--------"""

"""Write a function to find length of a string (without using len())."""

# def count_length(name):
#     count = 0
#     s = " "
#     for i in name:
#         s += i
#         count +=1
#     print(count)

# s = input("Enter a string anything :- ")
# count_length(s)

# n = input("Enter a string anything :- ")
# count = 0
# s = " "
# for i in n:
#     s += i
#     count +=1
# print(count)

"""Create a function to count vowels in a string."""
# s = "laxit"
# count_vowels = 0
# for i in s:
#     if i in "aeiouAEIOU":
#         count_vowels +=1
# print(count_vowels)       

# def count_vowels(s):
#     count = 0
#     for i in s:
#         if i in "AEIOUaeiou":
#             count +=1
#     print(count)        

# s = input("Enter a string anything :- ")
# count_vowels(s)


"""Write a function to count consonants in a string."""
# def count_consonants(s):
#     count = 0
#     for i in s:
#         if i not in "AEIOUaeiou":
#             count +=1
#     print(count)        

# s = input("Enter a string anything :- ")
# count_consonants(s)

"""Create a function to reverse a string."""
"""Method 1"""
# def reverse_string(s):
#     rev = s[::-1]
#     print(rev)

# s = input("Enter a string :- ")
# reverse_string(s)    

"""Method 2 """
# def reverse_string(s):
#     rev = " "
#     for i in s:
#         rev = i+ rev
#     print(rev)

# s = input("Enter a string :- ")
# reverse_string(s)

"""method 3"""
# def reverse_string(s):
#     rev = ""
#     for i in range(len(s)-1,-1,-1):
#         rev += s[i]
#     print(rev)    
# s = input("Enter a string :- ")
# reverse_string(s)

"""Write a function to check if a string is palindrome."""  
# s = "naman"
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev += s[i]

# if rev == s:
#      print("String is a palindrome")
# else:
#     print("String is not palindrome")    

# def string_palindrome(s):
    
#     rev = ""
#     for i in range(len(s)-1,-1,-1):
#         rev += s[i]

#     if rev == s:
#         print("String is a palindrome")
#     else:
#         print("String is not palindrome")    

# s = input("Enter a string :- ")
# string_palindrome(s)


"""Create a function to convert string to uppercase."""

# def to_uppercase(s):
#     result = ""
    
#     for ch in s:
#         if 'a' <= ch <= 'z':   
#             result += chr(ord(ch) - 32)
#         else:
#             result += ch
    
#     return result


# print(to_uppercase("laxit"))   



"""Write a function to convert string to lowercase."""
# def to_lowercase(s):
#     result = ""
    
#     for ch in s:
#         if 'A' <= ch <= 'Z':   # check uppercase
#             result += chr(ord(ch) + 32)
#         else:
#             result += ch
    
#     return result


# print(to_lowercase("LAXIT"))   

"""Create a function to count words in a string."""

# def  count_words(s):
#     count = 0
#     rev = ""
#     for i in s:
#         rev +=i
#         count+=1
#     print(count)    

# count_words("Laxit")    


"""Write a function to remove spaces from a string."""
"""Method 1"""
# s = "Laxit Dange"
# result = ""
# for ch in s:
#     if ch !=" ":
#         result +=ch
# print(result)   
"""Using function"""     
# def remove_Space(s):
#     result = ""
#     for ch in s:
#         if ch !=" ":
#             result +=ch 
#     return result 
# s = input("Enter a string :- ")
# print(remove_Space(s))

"""Methode 2"""
# s= "LAXIT Dange"
# s.replace(" ","")
# print(s)

"""Using function"""
# def remove_space(s):
#     return s.replace(" ", "")


# print(remove_space("L AXIT D ANGE"))

# Create a function to count frequency of a character.

# s = "banana"
# ch = "a" // i check a frequency of a in banana means count the a in banana 

# count = 0
# for c in s:
#     if c == ch:
#         count += 1
# print("Frequency =", count)
"""Method 1"""
# def count_frequency(s,ch):
#     count = 0
#     for c in s:
#         if c == ch:
#             count +=1
#     print("Frequency =", count)        

# count_frequency("naman","n")

"""Method 2"""

# def count_frequency(s,ch):
#    return s.count(ch)
    
# print(count_frequency("banana" ,"a"))   
 



"""---------------------Advanced Level (41–50)----------------"""

"""Write a function to swap two numbers."""
"""Methode 1"""
# def swap_two_number(num1,num2):
#     temp = num1
#     num1 = num2
#     num2 = temp
#     return num1 , num2

# a,b = swap_two_number(12,13)
# print(a,b)

"""Methode 2"""
# def swap_two_number(num1,num2):
#     num1,num2 = num2 , num1
#     print(num1,num2)
# swap_two_number(1,2)    

"""Methode 3"""
# def sawp_two_numbe(num1,num2):
#     return num2 , num1
# a , b = sawp_two_numbe(1,2)
# print(a,b)

"""Create a function to check Armstrong number."""
# def Armstrong(n):
#     n = str(n)
#     length = len(n)
#     n = int(n)
#     cube_sum = 0
#     temp = n
#     while temp>0:
#         last_digit = temp %10
#         cube_sum += last_digit**length
#         temp //=10

#     if n == cube_sum:
#         print("Number is Armstrong")
#     else:
#         print("Number is not Armstrong")        

# Armstrong(145)    
# Armstrong(153)



"""Write a function to print all prime numbers in a range."""
# def prime_number(n):
#     for i in range(2,n+1):
#         a = i
#         for j in range(2,(a//2)+1):
#             if a%j==0:
#                 break
#         else:
#             print(i,end=" ")

# n = int(input("Enter a number :- "))
# prime_number(n)                

"""Create a function to find sum of even digits in a number."""
# def sum_even(n):
#     even_sum = 0
#     for i in range(1,n+1):
#         if i%2 == 0:
#             even_sum += i
#     return even_sum

# n = sum_even(10)
# print(n)        

"""Write a function to find sum of odd digits in a number."""

# def sum_odd(n):
#     odd_sum = 0
#     for i in range(1,n+1):
#         if i%2 != 0:
#             odd_sum += i
#     return odd_sum

# n = sum_odd(10)
# print(n)     

"""Create a function to check perfect number."""
# def perfect_number(n):
#     sum_fact = 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum_fact +=i
#     if n == sum_fact:
#         print("Number is perfect ")
#     else:
#         print("Number is not perfect ")

# perfect_number(6)    


"""Write a function to print pattern using function."""

"""Create a function to calculate simple interest."""

# Write a function to calculate area of circle.
# Create a function to check whether a number is positive, negative, or zero.