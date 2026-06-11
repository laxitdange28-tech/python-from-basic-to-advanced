"""1. Floyd’s Triangle"""
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n = int(input("Enter a number :- "))
# num = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()    

"""reverse Triangle"""
# 1 2 3 4 
# 5 6 7
# 8 9
# 10
# n = int(input("Enter a number :- "))
# num = 1
# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print(num ,end=" ")
#         num +=1    
#     print()    

""" Pascal’s Triangle num = num * (i - j) // (j + 1)"""
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1

# n =int(input("Enter a number :- "))
# for i in range(n):
#     num = 1
#     for j in range(i+1):
#         print(num , end=" ")
#         num = num * (i - j) // (j + 1)
#     print()    

# * 
# * *
# * * *
# * * * *
# * * * * *

# n = int(input("Enter a number :- "))

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    

# * * * * * 
# * * * *
# * * *
# * *
# *

# n = int(input("Enter a number :- "))

# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print("*" , end=" ")
#     print()    

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print() 

# 0 
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(j,end=" ")
#     print() 


# A 
# B C 
# D E F 
# G H I J 
# K L M N O 

# n = int(input("Enter a number :- "))
# num = 65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(num),end=" ")
#         num +=1
#     print()    


# A 
# B B 
# C C C 
# D D D D 

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#     print()  

# A 
# A B 
# A B C 
# A B C D 
# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()


# ---------------- rectangl -----------------
# * * * * * * 
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(n+1): 
#         print("*",end=" ")
#     print()    

# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# n = int(input("Enter a number :- "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i , end=" ")
#     print()    
"""
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5"""
# n = int(input("enter a number :- "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()    

# 1 1 1 1 
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1

# n = int(input("enter a number :- "))
# num =1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(num,end=" ")
        
#     print()  


# 1 2 3 
# 4 5 6
# 7 8 9

# n = int(input("enter a number :- "))
# num =1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(num,end=" ")
#         num +=1
        
#     print()  

# print(ord('Z'))
# print(chr(65))

# A B C D E 
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# n = int(input("Enter  a number :- "))
# for i in range(1,n+1):
#     num =65
#     for j in range(1,n+1):
#         print(chr(num),end=" ")
#         num+=1
#     print()    


# A A A A
# B B B B 
# C C C C 
# D D D D

# n = int(input("Enter a number :- "))
# num = 65   
# for i in range(n):
#     for j in range(n):
#         print(chr(num), end=" ")
#     num += 1   
#     print()

# A B C D E 
# F G H I J
# K L M N O
# P Q R S T
# U V W X Y

# n = int(input("Enter a number :- "))
# num = 65
# for i in range(n):
#     for j in range(n):
#         print(chr(num), end=" ")
#         num += 1
#     print()















