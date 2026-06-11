"""----Basic Level (1–10)----"""
"""What is a list in Python? How is it different from a tuple?"""
# List --> list is a data structure store all type of data and list is a mutable and  allowe  duplicated and orders this is called list 
# tuple --> tupel is a orderd but not mutable they are fixe this is called  tuble
        
"""How do you create an empty list?"""
# list1 = []
# print(type(list1))
# if not list1:
#     print("List is empty")
# else:
#     print("list is not empty")    

"""Write a program to find the length of a list."""
# l = [1,2,3,4,5]
# print(len(l))

"""How do you access elements in a list using indexing?"""
# l = [1,2,3,4,5]
# a = l[0] #access elements using indexing
# print(a)

"""What is negative indexing in a list?"""
# l = [1,2,3,4,5]
# a = l[-4:-1] # 2 , 3 , 4
# print(a)

"""Write a program to add an element at the end of a list."""
# l = [1,2,3,4,5]
# l.append(6)
# print(l)

"""How do you insert an element at a specific position?"""
# l = [1,2,3,4,5,10,9]
# l.insert(5,9)
# # a=l.index(10) #check index number
# print(l)

"""Write a program to reverse an element from a list."""
"""Method 1"""
# l = [1,2,3,4]
# rev = l[::-1]
# print(rev)
"""Methode 2 """
# l = [1,2,3,4,5]
# l.reverse()
# print(l)

# l = [1,2,3,4,5]
# rev = []
# for i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
# print(rev)    

"""What is the difference between remove() and pop()"""
# remove --> remove first occurrence of value 
# pop --> remove last element 

"""remove()"""
# l = [1,2,3,4,5]
# l.remove(2)
# print(l)

"""pop()"""
# l = [1,2,3,4,5]
# l.pop()
# print(l)

"""How do you check if an element exists in a list?"""

# l = [1,2,3,4,5]

# if 3 in l:
#     print("-----Element exists----")
# else:
#     print("----Element not exsit-----")    

"""----Intermediate Level (11–20)----"""

"""Write a program to find the maximum and minimum element in a list."""
# l = [12,1,34,1,4]
# max_element = l[0]
# min_element = l[0]
# for i in l:
#     if max_element < i:
#         max_element = i
#     elif min_element >i:
#         min_element = i  
# print(f"maximum element = {max_element}")   
# print(f"minimum element = {min_element}")

"""How do you reverse a list? (without using built-in function)"""
"""Method 1"""
# l = [1,2,3,4]
# rev = []
# for i in l[::-1]:
#     rev.append(i)

# print(rev)   
"""Method 2""" 
# l = [1,2,3,4]
# rev = []
# for i in l:
#     rev.insert(0,i)

# print(rev) 

"""method 3"""
# l = [10,20,30,40]
# j = len(l)-1
# for i  in range(len(l)//2):
#     l[i],l[j]=l[j],l[i]
#     j -=1
# print(l)

"""Write a program to sort a list in ascending order."""
"""method 1"""
# l = [9,3,5,1,4,10]
# l.sort()
# print(l)

"""Method 2 selection sort """
# l = [9,3,5,1,4,10]

# for i in range(len(l)):
#     min_index = i
#     for j in range(i+1,len(l)):
#         if l[j] < l[min_index]:
#             min_index = j
#     l[i] , l[min_index] = l[min_index],l[i]        

# print(l)

"""prectice 1"""
# l = [9,3,5,1,4,10]
# n = len(l)
# for i in range(n):
#     min_index = i
    
#     for j in range(i+1,n):
#         if l[j] <l[min_index]:
#             min_index = j

#     l[i],l[min_index] = l[min_index] , l[i]       

# print(l)

"""prectice 2"""
# l = [9,3,5,1,4,10]
# n = len(l)
# for i in range(n):
#     min_index = i

#     for j in range(i+1,n):
#         if l[j] < l[min_index]:
#             min_index = j 

#     l[i],l[min_index] = l[min_index] ,l[i]

# print(l)


"""sotr a list usting functin and slection sort algoritham """

# def sort_list(l):
#     n = len(l)

#     for i in range(n):
#         min_index = i

#         for j in range(i+1,n):
#             if l[j] < l[min_index]:
#                 min_index = j 
#         l[i] , l[min_index] = l[min_index] , l[i]  

#         return l        
    
# l = [9,3,5,1,4,10]
# print(sort_list(l))

"""user input a list """
"""Methode 1"""
# n = int(input("Enter a size of list :- "))
# l = []

# for i in range(n):
#     x = int(input())
#     l.append(x)

# print("Your list is = ",l)

"""Methode 2 """
# l = eval(input("Enter a list :- "))
# print(f"Your list is =  {l}")

"""Methode 3 """
# l = list(map(int,input("Enter a list element :- ").split(",")))           
# print(l)


"""Write a program to count occurrences of an element in a list."""
# l = [1,2,3,4,5,2,2,3,8,3,4,3]
# print(f"Your list is {l} tell me which element is count  ")
# n = int(input("Enter a element to count in list :- "))
# count= l.count(n)
# print(f"{n} is presence in list in  {count} times ")

"""How do you copy a list? Explain shallow copy vs deep copy."""
"""Ways to Copy a List"""
"""shallow copy"""
""" 1. Using copy() method"""
# l1 = [1,2,3,4]
# l2 = l1.copy()

"""2. Using slicing"""
# l1 = [1,2,3,4]
# l2 = l1[::]

"""3.Using list() constructor"""
# l1 = [1,2,3,4]
# l2 = list(l1)
# print(l2)

"""Reference copy of a list 1 ka """
# l1 = [1,2,3,4]
# l2 = l1 
# l2[0]=100 # change list 1 

"""Shallow Copy --> Shallow copy ek nayi list banata hai, lekin uske andar ke elements same memory reference share karte hain. """

""" Agar list nested nahi hai → shallow copy safe
 Agar list nested hai → deep copy use karo"""

# simple list
# l1 = [1,2,3,4,5]
# l2 = l1.copy()
# l2[0] = 100 # Not change oreganal copy it is safe
# print(l1)

# nested list 
# l1 = [1,2,[3,4]] #Agar list nested hai → deep copy use karo
# l2 = l1.copy()

# # Case 1: outer change
# l2[0] = 100
# print(l1)  # [1, 2, [3, 4]] ✅ no effect

# # Case 2: inner change
# l2[2][0] = 999
# print(l1)  # [1, 2, [999, 4]] ❌ changed!

"""Deep Copy --> Deep copy ek completely nayi list banata hai, aur uske andar ke saare elements (including nested) bhi naye banata hai  """                    

# import copy

# l1 = [1,2,[3,4]]
# l2 = copy.deepcopy(l1)

# l2[2][0]=99
# print(l1) #no change oreganal list

# print(l2) # change only copy 

"""Write a program to merge two lists."""  
"""Method 1"""
# l1 = [1,2,3]
# l2 = [4,5,6]
# l1.extend(l2)
# print(l1)
"""Method 2"""
# l1 = [1,2,3]
# l2 = [4,5,6]

# l1.append(l2)
# print(l1)
"""Method 3"""
# l1 = [1,2,3]
# l2 = [4,5,6]

# l3 = l1 + l2
# print(l3)

"""Method 4"""
# l1 = [1,2,3]
# l2 = [4,5,6]

# for i in l2:
#     l1.append(i)

# print(l1)               

"""Write a program to remove duplicates from a list."""   
"""Method 1"""  
# l = [1,2,3,2,3,2]
# result = []
# for i in l:
#     if i not in result:
#         result.append(i)

# print(result)

"""Method 2"""
# l = [1,2,3,2,3,2]
# l = list(set(l))
# print(l)

"""Method 3 """
# l = [1,2,3,2,3,2]
# for i in range(len(l)):
#     j = i+1
#     while j<len(l):
#         if l[i] == l[j]:
#             l.pop(j)
#         else:
#             j +=1    

# print(l)

"""How do you slice a list? Explain with examples."""     
# ist ka kuch hissa (portion) nikalna

# l = [1,2,3,4,5,6,7,8,9,10]
# s = l[3:8]
# print(s)

# l = [1,2,3,4,5,6,7,8,9,10]
# rev = l[::-1]
# print(rev) 


"""Write a program to find the sum of all elements in a list.  """   
# l = [1,2,3,4,5]
# sum = 0
# for  i in l:
#     sum +=i 
# print(sum)    


"""Write a program to find the second largest number in a list. """     

# l = [1,2,3,4,5]

# max_element = l[0]
# second_max = l[0]


# for i in l:
#     if i > max_element:
#         second_max = max_element
#         max_element = i
#     elif i > second_max and i != max_element:
#         second_max = i

# print(second_max)


"""-------Advanced Level (21–30)-------"""

"""Write a program to rotate a list to the right by k steps."""
# l = [1,2,3,4,5]
# k = 2
# k = k%len(l)
# roteted = l[-k:] + l[:-k]
# print(roteted)

"""Write a program to find all pairs in a list whose sum is equal to a given number."""
# l = [1,2,3,4,5]
# target = 5
# n = len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         if l[i]+l[j] == target:
#             print(f"Pair: ({l[i]}, {l[j]})")

"""using two pointers """
# l = [2, 7, 11, 15] 
# target = 9

# left = 0
# right = len(l)-1

# while left<right:
#     s = l[left] + l[right]
    
#     if s ==target:
#         print(f"{l[left]} + {l[right]} = {target}")
#         break

#     elif s<target:
#         left +=1
#     else:
#         right -=1
"""Write a program to flatten a nested list."""
"""method 1"""
# l = [[1, 2], [3, 4], [5, 6]]
# flat =[]
# for i in l:
#     for j in i:
#         flat.append(j)
# print(flat)      
"""method 2"""
# l = [[1, 2], [3, 4], [5, 6]]
# flat = [j for i in l for j in i]
# print(flat)

"""Write a program to find the intersection of two lists."""
# l1 = [1,2,3,4,5]
# l2 = [1,3,6,8,9]
# result = []
# for i in l1:
#     if i in l2:
#         result.append(i)
# print(result)        

"""Write a program to check if a list is a palindrome."""
# l = [1,2,2,1]
# s = 0
# e = len(l)-1
# palindrome = True
# while s<e:
#     if l[s] != l[e]:
#         palindrome =False
#         break
#     s+=1
#     e-=1

# if palindrome:
#     print("List is palindrome")
# else:
#     print("List is not palindrome")        


"""Write a program to find the frequency of each element in a list."""
# l = [1,2,3,2,3,4,5]
# visited = []

# for i in range(len(l)):
#     if l[i] in visited:
#         continue
    
#     count = 1
#     for j in range(i + 1, len(l)):
#         if l[i] == l[j]:
#             count += 1
    
#     visited.append(l[i])
#     print(f"{l[i]} : {count}")

"""method 2"""
# l = [1, 2, 2, 3, 1, 2]

# freq = {}

# for i in l:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)

"""Write a program to separate even and odd numbers into two lists."""
# l = [1,2,3,4,5]
# even = []
# odd = []

# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(f"even list {even}")
# print(f"odd list {odd}")
    
    

"""Write a program to find the missing number in a list of 1 to n."""
# l = [1,2,3,5,7,9]
# n = max(l)
# for i in range(1,n+1):
#     if i not in l:
#         print(i)

"""Write a program to find the longest consecutive sequence in a list."""

# a = [1,2,3,7,8,9,10,11,55,13,14,15]

# a.sort()   
# count = 1
# l = []

# for i in range(len(a)-1):
#     if a[i+1] == a[i] + 1:
#         count +=1 
#     else:
#         l.append(count)
#         count = 1
# l.append(count)

# print(max(l))




# Write a program to implement a list without using built-in list methods.

"""-----------------------------------------------------------------"""
"""print positive and negative elements of an List"""
# l = [1,2,-3,4,-5,-9]
# positive = []
# negative = []

# for i in l:
#     if i>0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print(f" positive element in list {positive} \n negative element in list {negative} ")            

"""Mean of List elements"""
# l = [1,2,3,4,5]
# sum_list = 0

# n = len(l)
# for i in l:
#     sum_list+=i
# mean = sum_list/n
# print(mean)


"""Find the greatest element and print its index too"""
# l = [1,15,2,3,6]
# greatest_element = float('-inf')
# index = 0
# for i in range(len(l)):
#     if l[i]>greatest_element:
#         greatest_element = l[i]
#         index = i
# print(f"greatest element in list {greatest_element} and index number {index}")       

"""Find the second greatest element"""
"""not work any time """
# l = [1,2,3,4,5]
# greatest_element = l[0]
# second_greatest = l[0]

# for i in range(len(l)):
#     if l[i]>greatest_element:
#         second_greatest = greatest_element
#         greatest_element = l[i]
#     elif l[i]<greatest_element and l[i] != greatest_element:
#         second_greatest = l[i]   

# print(f" second greatest element = {second_greatest} \n greatest element = {greatest_element}")

"""Methode 2 work any time and any case"""
# l = [2, 96, 69, 77, 145, 20]

# l =  [145, 96, 69, 77, 142, 78]

# l = [90,16,17,23,2,89,45]

# greatest_element =  float('-inf')
# seconde_greatest_lement =  float('-inf')
# largest_index = second_index = -1

# for i in range(len(l)):
#     if l[i] > greatest_element:
#         seconde_greatest_lement = greatest_element
#         second_index = largest_index

#         greatest_element = l[i]
#         largest_index = i

#     elif l[i]>seconde_greatest_lement and l[i]!= greatest_element:
#         seconde_greatest_lement = l[i]
#         second_index = i
        
# print(f"Largest number in list = {greatest_element} Index: {largest_index}") 
# print(f"Second largest number in list = {seconde_greatest_lement} Index: {second_index}")

"""find smallest number and second smallest number in list  with index"""
# l = [12, 3, 111, 2, 15, 20]

# smallest = second_smallest = float('inf')
# smallest_index = second_index = -1

# for i in range(len(l)):
#     if l[i] < smallest:
#         second_smallest = smallest
#         second_index = smallest_index
        
#         smallest = l[i]
#         smallest_index = i
        
#     elif l[i] < second_smallest and l[i] != smallest:
#         second_smallest = l[i]
#         second_index = i

# print("Smallest:", smallest, "Index:", smallest_index)
# print("Second Smallest:", second_smallest, "Index:", second_index)


"""Check if List is sorted or not."""
# l = [1,2,13,4,5]
# list_sort = True
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         list_sort = False
#         break
# if list_sort:
#     print("List is sorted")    
# else:
#     print("List is not sorted")    

"""reverse a list"""
"""method 1"""
# l = [10,20,30]
# rev=[]
# for i in range(len(l)-1,-1,-1):
#     rev.append(i)
# print(l)

"""method 2"""
# l = [10,20,30,40]
# j = len(l)-1
# for i  in range(len(l)//2):
#     l[i],l[j]=l[j],l[i]
#     j -=1
# print(l)

"""method 3"""
# l = [10,20,30,40]
# rev = []
# for i in l:
#     rev.insert(0,i)

# print(rev)    

"""methode 4"""

# l = [10,20,30,40,50]
# for i in range(len(l)):
#     for j in range(len(l)-1-1):
#         l[i],l[j] = l[j],l[i]
        
# print(l)      


"""assign all the 0s at the end of the list"""

# l = [0,1,0,3,12,0,5,10] 
# j = len(l)-1
# i = 0
# while i < j:
#     if l[i]==0:
#         l[i],l[j] = l[j],l[i]
#         j -=1
#     else:
#         i +=1
# print(l)            
       
"""method 2"""
# j = 0 
# for i in range(len(l)):
#     if l[i] != 0 :
#         l[i],l[j] = l[j],l[i]
#         j = j+1
# print(l)   


"""Write a program to rotate a list to the right by k steps.""" 
# l = [1,2,3,4,5]
# k = 2 

# for i in range(k):
#     last_element = l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j] = l[j-1]
#     l[0] = last_element
# print(l)      


l = [1,2,3,4,5]
k = 2

n = len(l)
k = k % n   


i, j = 0, n-1
while i < j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1


i, j = 0, k-1
while i < j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1


i, j = k, n-1
while i < j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1

print(l)