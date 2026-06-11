"""1. Ask the user to enter a number and check if it is even or odd.
Input: 5 Output: """
# num = int(input("Enter a number :- "))
# print("Number is even" if num%2==0 else "Number is odd")

"""2. Ask the user to enter a number and check if it is positive, negative, or zero.
 Input: -2 Output:
 Negative"""
# n = int(input("Enter a number:- "))
# "Positive number"if n >=0 else "Nigative number"

"""3. Ask the user to enter two numbers and print the greater number.
 Input: 4, 7 Output: 7 is greater"""
# a = int(input("Enter a numberb :- "))
# b = int(input("Enter a number :- "))
# print("A is greater then B"if a>b else "B is greater then A" if a<b else "Both are equle")

"""4. Ask the user to enter a number and print numbers from 1 to that number using loop.
 Input: 5 Output: 1 2 3 4 5"""
# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     print(i)

"""5. Ask the user to enter a number and print its multiplication table.
Input: 3 Output: 3 x 1 = 3 ... 3 x
10 = 30"""
# n = int(input("enter a number and print its multiplication table :- "))
# for i in range(1,11):
#     print(f"{n} X {i} =  {n*i}")

"""6. Ask the user to enter a number and print sum from 1 to n.
Input: 5 Output: Sum = 15"""
# n =int(input("Enter number :- "))
# sum = 0
# for i in range(1,n+1):
#     sum +=i 
# print("Sum = ",sum)    
"""7. Ask the user to enter a number and check if it is divisible by 2 and 3.
 Input: 6 Output: Divisible"""
# n = int(input("Enter a number :- "))
# print("Number is divisible by both"if n %2==0 and n%3==0 else "Number is not divisible by both")
"""8. Ask the user to enter a number and count digits using loop.
Input: 1234 Output: Digits = 4"""
n = int(input("Enter a number:- "))
reverse = 0
count = 0
while n>0:
    last_Digit = n%10
    reverse = reverse*10 + last_Digit
    count +=1
    n//=10
    
print("reverse number = ", reverse,"Total digit = ",count)
# 9. Ask the user to enter a number and print reverse of number.
# Input: 123 Output: Reverse = 321
# 10. Ask the user to keep taking input until user enters 0 and print total sum



