"""1. Print numbers from 1 to 5 using a for loop.
Output: 1 2 3 4 5"""
# n = int(input("Enter a number :- "))
# for i in range(2,n+1):
#     a=i
#     for j in range(2,(a//2)+1):
#         if a%j==0:
#             break

#     else:    
#         print(i)

"""2. Print numbers from 1 to 10."""
"""Output: 1 2 3 4 5 6 7 8 9 10"""
# for i in range(1,11):
#     print(i)
"""3. Print even numbers from 1 to 10.
Output: 2 4 6 8 10"""
# for i in range(1,11):
#     if i %2==0:
#         print(i)
"""4. Print odd numbers from 1 to 10.
Output: 1 3 5 7 9"""
# for i in range(1,11):
    # if i %2!=0:
        # print(i)
"""5. Print numbers from 10 to 1 (reverse order).
Output: 10 9 8 7 6 5 4 3 2 1"""
# for i in range(10,0,-1):
#     print(i)
"""6. Print multiplication table of 2.
Output:
2 x 1 = 2
...
2 x 10 = 20"""

# n = int(input("Enter a number to print table : - "))
# print(f"Table of {n}")
# for i in range(1,11):
#     print(F"{i} X {n} = {i*n}")

"""1. Ask the user to enter a number and print sum of first n natural numbers.
Input: 5
Output: Sum = 15"""
# n = int(input("Enter a number :- "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(f"Sum = {sum} ")    

"""2. Ask the user to enter a number and print factorial of that number.
Input: 5
Output: Factorial = 120"""

# n = int(input("Enter a number :- "))
# factorial =1 
# for i in range(1,n+1):
#     factorial *= i
# print(f"factorial = {factorial}")    
"""3. Ask the user to enter a number and print all even numbers up to that number.
Input: 10
Output: 2 4 6 8 10"""
# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     if i %2 == 0:
#         print(i , end=" ")

"""4. Ask the user to enter a number and print all odd numbers up to that number.
Input: 10
Output: 1 3 5 7 9"""
# n = int(input("Tell me the range :- "))
# for i in range(1,n+1):
#     if i % 2 != 0:
#         print(i , end=" ")

"""5. Ask the user to enter a number and print numbers divisible by 5 up to that number.
Input: 20
Output: 5 10 15 20"""

# n = int(input("Enter a number : - "))
# for i in range(1,n+1):
#     if i % 5 == 0:
#         print(i , end=" ")

"""6. Ask the user to enter a number and print the sum of even numbers up to that number.
Input: 10
Output: Sum = 30"""

# n = int(input("Enter a number :- "))
# sum_even = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even +=i
# print(f"Sum of even number = {sum_even}")        

"""7. Ask the user to enter a number and print the product of numbers from 1 to n.
Input: 4
Output: Product = 24"""
# n =int(input("Enter a number :- "))
# product =1
# for i in range(1,n+1):
#     product *=i
# print(product)    

"""8. Ask the user to enter a number and print squares of numbers from 1 to n.
Input: 4
Output: 1 4 9 16"""

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     print(i**2 , end=" ")

"""9. Ask the user to enter a number and print sum of odd numbers up to n.
Input: 5
Output: Sum = 9"""
# n = int(input("Enter a number :- "))
# sum_odd = 0
# for i in range(1,n+1):
#     if i % 2 !=0:
#         sum_odd +=i
# print(f"sum of odd = {sum_odd}")        

"""10. Ask the user to enter a number and print reverse of that number using loop.
Input: 5
Output: Reverse = 5432"""
# n = int(input("Enter a number :- "))
# for i in range(n,1,-1):
#     print(i ,end="")



"""----------------- Practice Sheet – For Loop (Medium-Hard Level)------------------"""

"""1. Ask the user to enter a number and print all prime numbers up to that number.
Input: 10
Output: 2 3 5 7"""

# n = int(input("Enter a number :- ")) #1
# for i in range(2,n+1): #  i=2,3,4,5,6,7,8,9,10,11
#     is_prime = True

#     for j in range(2,i): # i =2 , j =2 loop chalega hi nahi
#         if i%j == 0:
#             is_prime = False 
#             break
#     if is_prime:
#         print(i,end=" ")        
    

"""2. Ask the user to enter a number and check if it is Armstrong number.
Input: 153
Output: Armstrong""" 

# n = int(input("Enter a number :- "))
# sum_qube = 0
# temp = n 
# l = len(str(n))
# while temp>0:
#     last_number = temp % 10
#     sum_qube += last_number **l
#     temp //=10

# if sum_qube==n:
#     print(f"{sum_qube} is a armestrong number")
# else:
#     print("Not a armestrong number ")        

"""3. Ask the user to enter a number and print the sum of digits using loop.
Input: 456
Output: Sum = 15"""

# n = int(input("Enter a number :- "))
# temp = n 
# sum_number =0 
# while temp> 0:
#     last_digit = temp % 10
#     sum_number += last_digit
#     temp //=10

# print(f"sum of {n} number = {sum_number}")

"""4. Ask the user to enter a number and print reverse of the number.
Input: 1234
Output: Reverse = 4321"""

# n = int(input("Enter a number :- "))
# temp = n
# rev = 0
# while temp>0:
#     last_digit = temp%10
#     rev = rev * 10 + last_digit
#     temp//= 10
# print(f"reverse numberb = {rev}")    


"""5. Ask the user to enter a number and check if it is palindrome.
Input: 121
Output: Palindrome"""

# n = int(input("Enter a number :- "))
# rev = 0 
# temp = n
# while temp> 0:
#     last_digit = temp%10
#     rev = rev *10 + last_digit
#     temp //=10
# if rev == n :
#     print("Number is palindrom")
# else:
#     print("Number is not palindrom")      
  
"""6. Ask the user to enter a number and print all numbers between 1 to n that are divisible
by both 3 and 5.
Input: 30
Output: 15 30"""

# n = int(input("Enter a number :- "))

# for i in range(1,n+1):
#     if i%3 ==0 and i % 5==0:
#         print(i,end=" ")


# n = int(input("Enter a number :- "))
# is_divisible = False
# for i in range(1,n+1):
#     if i%3 ==0 and i % 5==0:
#         print(i,end=" ")
#         is_divisible = True  
                   
# if  is_divisible== False:
#   print("not divisible by 5 and 3 ")   


# n = int(input("Enter a number: "))

# is_divisible = False
  
# for i in range(1, n + 1):
#     if i % 15 == 0:
#         print(i, end=" ")
#         found = True

# if not is_divisible:
#     print("No numbers divisible by both 3 and 5")



"""7. Ask the user to enter a number and print factorial using loop without using built-in
functions.
Input: 14
Output: Factorial = 87178291200"""
  
# n = int(input("Enter a  number :- "))
# fact = 1
# for i in range(1,n+1):
#     fact *=i
# print(f"fctorial of a number {n} = {fact}")



"""1. Ask the user to enter a number and print all prime numbers up to that number.
Input: 10
Output: 2 3 5 7"""
"Methode 2"
# n = int(input("Enter a number :- "))
# for i in range(2,n+1):
#     a=i
#     for j in range(2,(a//2)+1):
#         if a%j==0:
#             break

#     else:    
#         print(i)

"""using function"""
# def prime_number(n):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             break
#     else:
#         print(n,end=" ")    

# # prime_number(2)

# n = int(input("Enter a range :- "))
# for i in range(1,n+1):
#     prime_number(i)






 































