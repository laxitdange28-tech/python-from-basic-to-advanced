"""38) Accept List elements and reprint it"""
"""Method 1"""
# n = int(input(" Enter a size of list :- "))
# l = []
# for i in range(n):
#     x = int(input("Enter a number ;- "))
#     l.append(x)
    
# print(l)    

"""Methode 2"""
# l = eval(input("Enter a list eliment :- "))
# print(l)
    
"""Methode 3"""
# l = list(map(int,input("Enter a list element :- ").split(",")))
# print(l)


"""Print  List elements in reverse order"""
"""method 1"""
# l = [10,20,30,40]
# rev = l[::-1]
# print(rev)

"""method 2"""
# l = [10,20,30,40]
# rev = []
# for i in l:
#     rev.insert(0,i)
# print(rev)    

"""method 3"""

# l = [10,20,30,40]
# rev = []
# for i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
    
# print(rev)    

"""method 4"""
# l = [10,20,30,40]

# j = len(l)-1
# for i in range(len(l)//2):
#     l[i],l[j]=l[j],l[i]
#     j -=1
# print(l)    

"""method 5"""
# l = [10,20,30,40]

# for i in range(len(l)):
#     for j in range(len(l)-1-1):
#         l[i],l[j]=l[j],l[i]
# print(l)        

"""40) Print positive and negative elements of an List"""
# l = [1,-2,-3,4,-5,6]
# positive = []
# negative = []

# for i in range(len(l)):
#     if l[i]>0:
#         positive.append(l[i])
#     else:
#         negative.append(l[i])
# print(f" {positive} \n {negative}")        

"""method 2 """
# l = [1,-2,-3,4,-5,6]
# positive = []
# negative = []

# for i in l:
#     if i>0:
#         positive.append(i)
#     else:
#         negative.append(i)
        
# print(f" {positive} \n {negative}")

"""Print list in ascending or descending order"""
"""method 1 """
# l = [1,12,3,14,6,2,10]
# l.sort()
# print(l)

"""method 2"""
# l = [1,12,3,14,6,2,10]
# n = len(l)
# for i in range(n):
#     min_index = i
#     for j in range(i+1,n):
#         if l[j] < l[min_index]:
#             min_index = j
#     l[i],l[min_index] = l[min_index] , l[i]
# print(l)    

    
"""42) Accept size n from user and create a n size List then take n inputs into the and finally 
   Print the sum of all elements in the List in the following manner
   10 + 20 + 30 = 60"""

# n = int(input("Enter a size of list :- "))
# l = []
# for i in range(n):
#     x = int(input("Enter a number :-  "))
#     l.append(x)
# print(f"Your list is = {l}")    
# sum_list = 0
# for i in l:
#     sum_list +=i
# print(f"sum of list element = {sum_list}")    


# 43) Mean of List elements.
# l = [10,20,30,40]
# n = len(l)
# sum_element = 0
# for i in l:
#     sum_element +=i

# mean = sum_element / n
# print(f"Mean = {mean}")

"""44) Find the greatest element and print its index too.
  {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index"""
"""Method 1"""  

# l = [2, 96, 69, 77, 145, 20]
# greatest_element = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > greatest_element:
#         greatest_element = l[i]
#         index = i
# print(f"greatest element in list {greatest_element} index = {index}")    

"""method 2 """        
# l = [2, 96, 69, 77, 145, 200]
# greatest_element = l[0]

# for i in l:
#     if i > greatest_element:
#         greatest_element = i

# print(f"greatest element in list {greatest_element} ")        

"""45) Find the smallest element and print its index too.
   {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index"""
   
# l = [2, 96, 69, 77, 145, 20]
# smallest_elemen = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] < smallest_elemen:
#         smallest_elemen = l[i]
#         index = i
# print(f"greatest element in list {smallest_elemen} index = {index}")
    
"""46) Find the second greatest element0 
   {2, 96, 69, 77, 145, 20} = Second greatest element = 96"""
   
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


"""47Check if List is sorted or not.
"""
# l = [1,4,2,34,5,0]
# l = [1,2,3,4,5]
# is_sorted = True
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             is_sorted = False
#             break
# if is_sorted:
#     print("liist is sorted")
# else:
#     print("List is not sorted")


"""48) Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]"""

# l = [2,3,15,15,3,2]
# rev = []
# for i in l:
#     rev.insert(0,i)
# if l == rev:
#     print("list is psllindromic ")
# else:    
#      print("list are not psllindromic ")

"""---------- Practice Sheet – Lists ----------"""
""". Create a list of 5 numbers and print the list.
Output: [1, 2, 3, 4, 5]
"""
# l = [1, 2, 3, 4, 5]
# print(l)

"""2. Create a list of 3 fruits and print each item.
Output: apple banana mango"""

# l = ["apple" ,"banana" ,"mango"]
# print(l)

"""3. Create a list and print the first element.
Input: [10, 20, 30]
Output: 10"""

# l = [10, 20, 30]
# print(l[0])

"""4. Create a list and print the last element.
Input: [10, 20, 30]
Output: 30"""
# l =  [10, 20, 30]
# print(l[-1])

"""5. Create a list and print its length.
Input: [1, 2, 3, 4]
Output: Length = 4"""
# l = [1, 2, 3, 4]
# print(len(l))

"""6. Create a list and add a new element at the end.
Input: [1, 2, 3]
Output: [1, 2, 3, 4]"""
# l = [1, 2, 3]
# l.append(4)
# print(l)

"""7. Create a list and remove an element.
Input: [1, 2, 3, 4]
Output: [1, 3, 4]"""

# l = [1, 2, 3, 4]
# l.remove(4)
# print(l)

"""8. Create a list and check if a value exists in it.
Input: [10, 20, 30], check 20
Output: Present"""

# l = [10, 20, 30 ]
# for i in l:
#     if 20 in l:
#         print("present")
#         break


"""9. Create a list and print all elements using loop.
Input: [5, 6, 7]
Output: 5 6 7"""

# l = [5,6,7]
# for i in l:
#     print(i)

"""10. Create a list and print sum of all elements.
Input: [1, 2, 3]
Output: Sum = 6"""

# l = [1,2,3]
# sum = 0
# for i in l:
#     sum +=i
# print(sum)    


# Ş Practice Sheet – Lists (Medium Level)
"""1. Ask the user to enter a list of numbers and print the largest element.
Input: [2, 5, 1, 8]
Output: Largest = 8"""

# l = [2, 5, 1, 8]
# l = list(map(int,input("Enter a list element :- ").split(",")))
# largest = float('-inf')
# for i in l:
#    if  i > largest:
#       largest = i

# print(f"largest = {largest} ")       


"""2. Ask the user to enter a list and print the smallest element.
Input: [4, 2, 9, 1]
Output: Smallest = 1""" 
# l = [4, 2, 9, 1]
# l = list(map(int,input("Enter a list element :- ").split(",")))
# smallest = float('inf')
# for i in l:
#     if i< smallest:
#         smallest = i
# print(f"Smalest = {smallest}")        


"""3. Ask the user to enter a list and print sum of all elements.
Input: [1, 2, 3, 4]
Output: Sum = 10"""
# l = [1,2,3,4]
# sum = 0
# for i in l :
#     sum += i
# print(f"sum = {sum}")    

"""4. Ask the user to enter a list and count even numbers.
Input: [1, 2, 3, 4, 6]
Output: Count = 3"""
# l = [1,2,3,4,6]
# count = 0
# for i in l:
#     if i % 2==0:
#         count +=1
# print(f"Count = {count}")        

"""5. Ask the user to enter a list and count odd numbers.
Input: [1, 2, 3, 4, 5]
Output: 3"""
# l =  [1, 2, 3, 4, 5]
# count = 0
# for i in l :
#     if i % 2 !=0:
#         count +=1
# print(f"Count {count}")        

"""6. Ask the user to enter a list and reverse it.
Input: [1, 2, 3]
Output: [3, 2, 1]"""
"""method 1 """
# l = [10,20,30,40]
# reversed = []
# for i in l:
#     reversed.insert(0,i)
# print(reversed)    

"""method 2"""
# l = [10,20,30,40]
# j = len(l)-1
# for i in range(len(l)//2):
#    l[i] , l[j] = l[j], l[i]
#    j -=1
# print(l)   

"""method 3 time complexity high"""
# l = [10,20,30,40]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         l[i] , l[j] = l[j] , l[i]
# print(l)

"""7. Ask the user to enter a list and remove duplicates.
Input: [1, 2, 2, 3, 3]
Output: [1, 2, 3]"""
"""method 1"""
# l = [1, 2, 2, 3, 3]
# result = set(l)
# result = list(result)
# print(result)

"""method 2"""
# l = [1, 2, 2, 3, 3]
# result = []
# for i in l:
#     if i not in result:
#         result.append(i)
# print(result)   

"""method 3 """
# l = [1, 2, 2, 3, 3]     
# j = len(l)-1
# for i in range(len(l)-1):
#     if l[i] == l[j]:
#         l.pop()
#         j -=1
# print(l)        
      


"""8. Ask the user to enter a list and sort it in ascending order.
Input: [5, 2, 8, 1]
Output: [1, 2, 5, 8]"""
"""Bubble sort"""
# l = [5, 2, 8, 1] 
# for j in range(len(l)):
#    for i in range(len(l)-j-1):
#       if l[i] > l[i+1]:
#          l[i] , l[i+1] = l[i+1],l[i]

# print(l)
"""Slection sort"""
# l = [5, 2, 8, 1]

# for i in range(len(l)):
#    min_index = i
#    for j in range(i+1,len(l)):
#       if l[j] < l[min_index] :
#          min_index = j

#    l[i],l[min_index] = l [min_index] , l[i]  

# print(l)   


# 9. Ask the user to enter a list and find second largest element.
# Input: [10, 20, 4, 45]
# Output: 20
# 10. Ask the user to enter a list and print elements at even index.
# Input: [10, 20, 30, 40, 50]
# Output: [10, 30, 50]