"""Print numbers from 1 to 10 using a loop"""
# for i in range(1,11):
#     print(i)

# i = 1
# while i<=10:
#     print(i)
#     i +=1

"""Print numbers from 10 to 1 (reverse order)"""
# for i in range(10,0,-1):
#     print(i)

# i =10
# while i>0:
#     print(i)
#     i-=1

"""Print all even numbers from 1 to 20"""
# for i in  range(1,21):
#     if i%2==0:
#         print(i)

# i =1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i +=1    

"""Print all odd numbers from 1 to 20"""
# for i in  range(1,21):
#     if i%2!=0:
#         print(i)

# i =1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     i +=1  
"""Print multiplication table of a number"""
# n = int(input("Enter a number to print table :- "))
# print(f"Table of {n}")
# for i in range(1,11):
#     print(f"{i} X {n} = {i*n}")

# n = int(input("Enter number to print table :- "))
# i = 1
# while i<=10:
#     print(f"{i} X {n} = {i*n}")
#     i +=1

"""Find sum of numbers from 1 to n"""
# n = int(input("Entern a number to print sum :- "))
# sum = 0
# for i in range(1,n+1):
#     sum +=i
# print(sum)

# n = int(input("Enter a number to print sum :- "))
# i = 1
# sum =0
# while i<=n:
#     sum +=i
#     i +=1
# print(f"Sum = {sum}")    

"""Find factorial of a number"""
# n = int(input("Enter a number to find factorial :- "))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(f"Factorial = {fact}")   

# n = int(input("Enter a number to print a factorial :- "))
# fact = 1
# i = 1
# while i<=n:
#     fact*=i
#     i +=1
# print(f"Fctorial = {fact}")   
 
"""Count number of digits in a number"""
# n =int(input("Enter a digits :- "))
# count = 0
# for i in str(n):
#     n=int(n)
#     count+=1
# print(count)

# n =int(input("Enter a  digits:- "))
# count = 0
# while n>0:
#     last_digit = n%10
#     count +=1
#     n//=10
    
# print(f"count = {count}")    


    
"""Reverse a number using loop"""
# n = int(input("Enter a number :- "))
# revers = 0
# while n>0:
#     last_digit = n%10
#     revers = revers*10 + last_digit
#     n//=10
# print("Revers number = ",revers)    
"""Check if a number is palindrome"""
# n = (input("Enter a numbner : - "))
# revers = n[::-1]
# if int(n==revers):
#     print("number is palindrome ")
# else:
#     print("Not palindrome") 

# n = int(input("Enter a number :- "))
# temp =n
# revers = 0
# while temp>0:
#     last_digit = temp % 10
#     revers = revers *10 + last_digit
#     temp //= 10
# print(revers)
# if n == revers:
#     print("Number is palindrom")
# else:
#     print("Number is not palindrom")    

"""Print each character of a string using loop"""
# name = "Laxit"
# for i in name:
#     print(i)

# name = "laxit"
# n = len(name)
# i =  0
# while i<n:
#     print(name[i])
#     i +=1

"""Count vowels in a string
"""
# s = input("Enter a string :- ")
# count =0
# for i in s:
#     if(i in "AEIOUaeiou"):
#         count +=1
# print("Vowels = " , count)    

# s = input("Enter a string :- ")
# count = 0
# i =0
# while i<len(s):
#     if s[i] in "AEIOUaeiou":
#         count +=1
#     i +=1    
# print("Vowels = ",count)            2006  
"""Print squares of numbers from 1 to 10"""
# for i in range(1,11):
#     print(i**2)
"""Print cubes of numbers from 1 to 10"""
# for i in range(1,11):
#     print(i**3)
"""Print first n natural numbers"""
# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     print(i)
# -----------------------------------------------------------
# Find largest number in a list
# Find smallest number in a list
# Count even and odd numbers in a list
# Sum all elements of a list
# Print elements at even index positions
# Print elements at odd index positions
# Remove duplicates from a list using loop
# Find second largest number in a list
# Count frequency of each element in a list
""" Check if a number is prime"""
# n = int(input("Enter a number :- "))

# is_prime = True
# for i in range(2,n):
#     if n %i == 0:
#         is_prime = False
#         break

# if is_prime and n>1:
#     print("Number is prime")
# else:
#     print("Number is not prime ")   
#           
"""Print all prime numbers between 1 to 100"""
# for num in range(1,101):
#     if num >1:
#         for i in range(2,num):
#             if num %i==0:
#                 break
#         else:
#             print(num , end=" ")

"""Check if a number is Armstrong -> 153 , 1634"""
# n = int(input("Enter a number:- "))
# length =len(str(n))
# n = int(n)        
# temp = n
# # revers = 0
# arm = 0
# while temp>0:
#     last_digit = temp%10
#     arm += last_digit **length
#     # arm += revers **3
#     temp//=10

# if n == arm:
#     print("Number is Armstrong number")
# else:
#     print("Not Armstrong number ")    

"""Print Fibonacci series up to n terms"""
# n = int(input("Enter a number :- "))
# 0 , 1 , 1 , 2 , 3 , 5 ,8 ,13
# a = 0
# b = 1
# for i in range(1,n+1):
#     print(a,end=" ")
#     c  = a+b
#     a = b
#     b = c
"""Find GCD of two numbers using loop"""
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# gcd = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# print("GCD =", gcd)


"""Find LCM of two numbers using loop"""
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# max_num = max(a, b)

# while True:
#     if max_num % a == 0 and max_num % b == 0:
#         print("LCM =", max_num)
#         break
#     max_num += 1
        

"""Check if a number is perfect number"""
# n = int(input("Enter a number :- "))
# sum = 0 
# for i in range(1,n):
#    if n % i == 0:
#     sum += i

# if sum == n :
#     print("Number is perfect ")
# else:
#     print("Number is not perfect")   
    
"""Sum of digits of a number"""
# n = int(input("Enter a number:-  "))
# temp = n
# sum = 0
# while temp>0:
#     last_Digit = temp % 10
#     sum += last_Digit
#     temp //=10
# print(f"Sum of digits = {sum}")    

"""Product of digits of a number"""
# n = int(input("Enter a number:-  "))
# temp = n
# product = 1
# while temp>0:
#     last_Digit = temp % 10
#     product *= last_Digit
#     temp //=10
# print(f"Product of digits = {product}")    

# Find average of list elements
"""Convert decimal number to binary"""
# n = int(input("Enter a number :- "))
# binary = ""
# while n > 0:
#     remainder = n % 2
#     binary = str(remainder) + binary
#     n = n // 2

# print("Binary =", binary)

"""Print square star pattern
*****
*****
*****
*****
*****"""

# n = int(input("Enter a number :- "))
# for i in range(n):
#     for j in range(n):
#        print("*",end=" ")
#     print()    

"""Print right triangle pattern
*
**
***
****
*****"""
# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*" ,end=" ")
#     print()    

"""Print inverted triangle
*****
****
***
**
*"""
# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(n):
#         print("*" , end=" ")
#     n -=1
#     print()

# Print pyramid pattern
#     *
#    ***
#   *****
#  ******
# *******

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(n -i):
#         print(" " , end=" ")
#     n -=1
#     print() 

# n = 5

# for i in range(1, n + 1):
#     # print spaces
#     print(" " * (n - i), end="")
    
#     # print stars
#     print("*" * (2 * i - 1))


# n = 5

# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * (2*i - 1))




"""1 
2 3
4 5 6
7 8 9 10"""

# n  = int(input("Enter a number :- "))
# num= 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num +=1
        
#     print()


#     *    
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# n = int(input("Enter a number :- ")) 
# # Upper part
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))

# # Lower part
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "*"*(2*i-1))

"""2. Pascal’s Triangle
Output:
1
1 1
1 2 1
1 3 3 1"""

# n = int(input("Enter a number :- "))

# for i in range(n):
#     num = 1
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()


"""Hollow Square Pattern
Output:
*****
*   *
*   *
*   *
*****"""
# n = int(input("Enter a number :-  "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i ==  n-1 or j == 0 or j == n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")    
#     print()    

# X Pattern
# Output:
# *   *
#  * * 
#   *  
#  * * 
# *   *


# n = int(input("Enter anumber :- "))

# for i in range(n):
#     for j in range(n):
#         if i == j or j == n-i-1:
#             print("*" , end="")
#         else:
#             print(" ",end="") 
#     print()           


"""reverse string using loop"""
# s = input("Enter a string :- ")
# rev = ""
# for ch in s:
#     rev = ch + rev

# print("Reverse string = " , rev)   

# s = input("Enter a string:- ")
# for ch in range(len(s)-1,-1,-1):
#     print(s[ch],end="")

# s = input("Enter a string : - ")

# i = len(s)-1

# while i>=0:
#     print(s[i] , end="")
#     i -=1

"""Count all letters, digits, and special symbols from a given string Given: str1 = "P@#yn26at^&i5ve" Expected Outcome: Total counts of chars, digits, and symbols Chars = 8 Digits = 3 Symbol = 4"""

# str1 = "P@#yn26at^&i5ve"

# chars = 0
# digits = 0
# symbol = 0

# for ch in str1:
#     if (ch>= 'a' and ch<='z') or (ch>='A' and ch<='Z'):
#         chars +=1
#     elif ch>='0' and ch<='9':
#         digits +=1
#     else:
#         symbol +=1       

# print("chars = ",chars)
# print("digit = ",digits)
# print("symbol = ",symbol)

"""Print all the factors of a number"""
# n = int(input("Enter a number :- "))

# for i in range(2,n+1):
#     if n % i == 0:
#         print(i)

# n =int(input("Enter a number:- "))

# i = 2
# while i <=n:
#     if n %i ==0:
#         print(i)
#     i+=1    


""" strong number  -> 145 = 1! + 4! + 5! """  

# n = int(input("Enter anumber :- ")) 
# temp = n
# sum_fact = 0
# while temp>0:
#     last_digit = temp%10
#     fact = 1
#     for i in range(1,last_digit+1):
#         fact *= i 
#     sum_fact +=fact
#     temp//=10

# if sum_fact == n:
#     print(f"{sum_fact} is a stromg number ")

# else:
#     print(f"{sum_fact} is Not a strong number ")

#  Armstrong number --->   153 = 1^3 + 5^3 +3^3

# n = int(input("Enter a number :- "))
# temp = n 
# sum_qube = 0
# while temp>0:
#     last_digit = temp % 10
#     sum_qube += last_digit **3
#     temp //= 10

# if sum_qube == n:
#     print(f"{sum_qube} is Armstrong number") 

# else:
#     print(f"{sum_qube} is Not Armstrong number")    

"""check number is prime or not user input """

# n = int(input("Enter a number :- "))
# is_prime= True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime == False
#         break

# if is_prime:
#     print("Number is prime")
# else:
#     print("Number is not prime")    


"""Check number is palidrom or not user input"""
# n = int(input("Enter a number :- "))
# n = str(n)
# rev =  n[::-1]

# if rev==n:
#     print("number is palidrom ")
# else:
#     print("Number is not palidrom")    

# n = int(input("Enter a number :- "))
# temp = n
# revers = 0
# while temp>0:
#     last_number = temp %10
#     revers = revers*10 + last_number
#     temp //= 10


# print(revers)


    
"""Q1. Reverse a number
Example: 423 → 324

Sample Input:
Enter a number: 423

Sample Output:
Reversed number: 324"""

# n =int(input("Enter a number :- "))
# rev=0
# while n>0:
#     rev = rev *10 + n%10
#     n//=10 

# print(rev)    

"""Q2. Fibonacci series upto N terms
Example: n = 5 → 0 1 1 2 3

Sample Input:
Enter number of terms: 5

Sample Output:
Fibonacci series: 0 1 1 2 3"""

# n = int(input("Fibonacci series upto N terms :- "))

# a =0
# b = 1
# for i in range(1,n+1):
#     c = a+b
#     print(a,end=" ")
#     a=b
#     b=c


# n = int(input("Fibonacci series upto N terms :- "))
# a =0
# b = 1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b = b,a+b

"""Q3. Print the largest digit in a number
Example: 9482 → 9

Sample Input:
Enter a number: 9482

Sample Output:
Largest digit: 9"""

# n = int(input("Enter a number :- "))
# largest_digit = 0
# for i in str(n):
#     i = int(i)
#     if largest_digit <i:
#         largest_digit = i

# print(f"largest digit {largest_digit}")

"""
Q5. Check whether a number is paillndrom or not

Sample Input:
Enter a number: 1221

Sample Output:
Number is 1221 is Paillndrom"""

# n = int(input("Entre a number : -  "))
# temp = n 
# rev = 0
# while temp>0:
#     rev = rev  * 10 + temp % 10
#     temp //=10

# if rev == n :
#     print("--Number is palindrome😆--")    
# else:
#     print("number is not palindrome")    


"""Q6. Keep taking input until user enters 0, then print sum

Sample Input/Output:

Enter number: 5
Enter number: 3
Enter number: 2
Enter number: 0
Sum: 10"""

# sum = 0
# while True:
#     n = int(input("Enter a numbe :- "))
#     if n!=0:
#         sum+=n
#     else:
#         break    
    
# print(f"Sum of n number = {sum}")        


"""Q7. Reverse a number using while loop

Sample Input:
Enter a number: 1234

Sample Output:
Reversed number: 4321"""

# n =int(input("Enter a number :- "))
# rev=0
# while n>0:
#     rev = rev *10 + n%10
#     n//=10 

# print(rev) 


"""Q8. Count number of digits using while loop8

Sample Input:
Enter a number: 56789

Sample Output:
Number of digits: 5"""

# n = int(input("enter a digit :- "))
# count_digit = 0
# for i in str(n):
#     count_digit +=1

# print(count_digit)    

