"""1. Ask the user to enter a number and check if it is positive.
Input: 5
Output: Positive"""
# num = int(input("Enter a number :- "))
# if num>=0:
#     print("Number is positive")
# else:
#     print('Number is nagative')   
#  
"""2. Ask the user to enter a number and check if it is negative.
Input: -3
Output: Negative"""

# num = int(input("Enter a number:-  "))
# if num<0:
#     print("Number is nagative")
# else:
#     print("Number is positive ")    
"""3. Ask the user to enter a number and check if it is even or odd.
Input: 4
Output: Even"""

# num = int("Enter a number :- ")
# if num %2==0:
#     print("Number is even")
# else:
#     print("Number is odd")    
"""4. Ask the user to enter a number and check if it is greater than 10.
Input: 12
Output: Greater than 10"""
# num = int(input("Enter a number :- "))
# if num>10:
#     print("Number is greater then 10")
# else:
#     print("Number is less then 10")    
"""5. Ask the user to enter a number and check if it is equal to 0.
Input: 0
Output: Zero"""
# num = int(input("Enter a number :- "))
# if num ==0: 
#     print("number is equle to the 0")
# else:
#     print("Number is not equle to zero")    

"""6. Ask the user to enter two numbers and print the greater number.
Input: 5, 8
Output: 8 is greater"""
# a = int(input("Tell me 1st number :- "))
# b = int(input("Tell me 2nd number :- "))
# if a>b:
#     print("a is greter then b")
# elif b>a:
#     print("b is greter then a")
# else:
#     print("Both are equle")        

"""7. Ask the user to enter two numbers and print the smaller number.
Input: 5, 8
Output: 5 is smaller"""
# a = int(input("Tell me 1st number :- "))
# b = int(input("Tell me 2nd number :- "))
# if a<b:
#     print("a is smaller then b")
# elif b<a:
#     print("b is smaller then a")
# else:
#     print("Both are equle")  
"""8. Ask the user to enter their age and check if they are eligible to vote.
Input: 18
Output: Eligible"""
# age = int(input("Tell me your age :- "))
# if age>=18:
#     print("Your are eligible for vote")
# else:
#     print("Your are not eligible of vote")

"""9. Ask the user to enter a number and check if it is divisible by 5.
Input: 10
Output: Divisible"""
# num = int(input("Tell me number :- "))
# if num%5==0:
#     print("Number is divisible by 5")
# else:
#     print("Number is not divisible by 5")    
"""10. Ask the user to enter a number and check if it is divisible by 2 and 3.
Input: 6
Output: Divisible by both"""
# num = int(input("Tell ne number :- "))
# if num %2==0 and num%3==0:
#     print("Number is divisible by both 2 and 3")
# else:
#     print("Number is not divisible both 2 and 3  ")    
"""11. Ask the user to enter marks and check pass or fail (pass if ≥ 40).
Input: 45
Output: Pass"""
# marks =int(input("Tell me the your marks :- "))
# if marks>=40:
#     print("Your are pass")
# else:
#     print("You are fail")    
"""12. Ask the user to enter a number and check if it is between 1 and 100.
Input: 50
Output: In range"""
# number = int(input("Tell me number :- "))
# if number>1 and number<100:
#     print("Number is between 1 and 100 ")
# else:
#     print("Number is not between 1 and 100")    
"""13. Ask the user to enter temperature and check if it is hot (>30) or cold.
Input: 35
Output: Hot"""
# tempreture =  int(input("Tell me temparetute :- "))
# if tempreture >30:
#     print("Hot")
# else:
#     print("Cold")    
"""# 14. Ask the user to enter a number and check if it is multiple of 10.
# Input: 20
# Output: Multiple of 10"""
# number = int(input("Tell me the number :- "))
# if number%10==0:
#     print("Number is multiple of 10")
# else:
#     print("Number is not multiple by 10")    
"""15. Ask the user to enter a number and check if it is less than 0, equal to 0, or greater
than 0.
Input: -2
Output: Negativ"""
while True:
    number = int(input("Tell me the number :- "))
    if number<0:
        print("Negitive")
    elif number==0:
        print("Number is zerooooo")
    else:
        print("Number is positive")   
        
    choice = int(input("Enter your choice [0 No / 1 Yes] :- "))
    if choice==0:
        print("---Code is end---")
        break

    