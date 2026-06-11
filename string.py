"""31) Print string in reverse,its length,in uppercase,lowercase and copy into another string"""
# s = "Laxit"
# rev = s[::-1]
# print(rev)
# upper = s.upper()
# print(upper)
# lower = s.lower()
# print(lower)

"""32) Arrange string characters such that lowercase letters should come first"""
# s = "LaXit"
# lower = " "
# upper = ""

# for i in s:
#     if i.islower():
#         lower += i
#     else:
#         upper += i

# print(lower+upper)

"""33) Count all letters, digits, and special symbols from a given string
#     Given: str1 = "P@#yn26at^&i5ve"
#     Expected Outcome:
#     Total counts of chars, digits, and symbols
#     Chars = 8
#     Digits = 3
#     Symbol = 4"""

"""Method 1"""
# str1 = "P@#yn26at^&i5ve"
# Chars = 0
# Digits = 0
# Symbol = 0

# for i in str1:
#     if i.isdigit():
#         Digits +=1
#     elif i.isalpha():
#         Chars +=1
#     else:
#         Symbol +=1
# print(Chars)
# print(Digits)
# print(Symbol)


"""Method 1"""
# str1 = "P@#yn26at^&i5ve"
# Chars = 0
# Digits = 0
# Symbol = 0

# for i in str1:
#     if (i>='A' and i<='Z') or (i>='a' and i<='z'):
#         Chars +=1
#     elif i >='0' and i<='9':
#         Digits +=1
#     else:
#         Symbol +=1

# print(Chars)
# print(Digits)
# print(Symbol)


"""34) Compare two strings without using inbuilt functionsx """

# str1 = "Laxit"
# str2 = "Laxit"

# if len(str1)==len(str2):
#     for i in range(len(str1)):
#         if str1[i]!=str2[i]:
#             print("String not same")
#     else:
#         print("String are same")
# else:
#     print("Both length are not same ")                

"""35 Count Vowels from given string"""
# s = "laxit"
# count = 0
# for i in s:
#     if i in "AEIOUaeiou":
#         count +=1
# print(count)    

"""Using function"""
# def count():
#     s = "laxit"
#     count = 0
#     for i in s:
#         if i in "AEIOUaeiou":
#             count +=1
#     return count

# print(count())

"""36 Reverse a string"""
"""method 1"""

# s = "Laxit"
# rev = ""

# for i in range(len(s)-1,-1,-1):
#     rev +=s[i]
# print(rev)

# s = "Laxit"
# rev =""
# for i in s[::-1]:
#     rev = rev + i
# print(rev)    

     
"""method 2"""
# s = "Laxit"
# print(s[::-1])

"""method 3"""
# s = "Laxit"
# rev = ""
# for i in s[::-1]:
#     rev = rev + i
# print(rev)

"method 4"
# s = "Laxit"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)


"""37) Check string is Pallindrome or not**"""
# s = "naman"
# rev = ""

# for i in s:
#     rev = i + rev
# if rev == s:
#     print("palindrom")    
# else:
#     print("Not palindrom")

# s1 = "laxit"
# s2 = "laxit"

"""method using function"""
# def paliondrom(s):   
#     rev = ""

#     for i in s:
#         rev = i + rev
#     if rev == s:
#         print("palindrom")    
#     else:
#         print("Not palindrom")

# paliondrom("naman")   

"""34) Compare two strings without using inbuilt functionsx """
# if len(s1) == len(s2):
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             print("Not both are same")
#             break
#     else:
#         print("Both are same ")    
# else:
#     print("Not both are same")

"""Count the total vowel and total consonent"""
# s ="Laxit"
# cout1 = 0
# count2 = 0
# for i in s:
#     if i in "AEIOUaeiou":
#         cout1 +=1
#     else:
#         count2 +=1    
# print(cout1)
# print(count2)




