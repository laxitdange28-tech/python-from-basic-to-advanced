"""List[] -> is a data structure thay are mutable and order and store multipul datatype in a single list and Allows duplicates"""

# list1 = ["Laxit" , 20 , 22.0 ]

# print(list1)    # print hole listn whit []
# print(list1[0]) # indexing using and start from 0
# for i in list1:
#     print(i)    # print list element using for loop 
# list1[0]="Dange"  #update the value of index value 0 laxit to dange 
# print(list1[0])
# print(list1)     #change oregnal list value

"""-------😃List Methods😀---------"""

"""1) append() -> add element at the end"""
# list1 = [1 , 2 , 3]
# list1.append(4) # -----> add element at the end
# print(list1)

"""2) insert() ->Adds element at a specific position"""
# list1 = ["laxit" , 12 ,30 ]
# list1.insert(1,"dange") # (index number , value)
# print(list1)

"""3) extend()--->Adds multiple elements (another list)"""
# list1 = [1,2,3]
# list1.extend([4,5,6 ,"hi"]) # add another list 
# print(list1)

"""4) remove()--> Removes first occurrence of value"""
# list1 = [1,2,3]
# list1.remove(1)
# print(list1)

"""5) pop() --> Removes element using index -->(Default: last element)"""
# list1 = [1,2,3]
# list1.pop() #(Default: last element)
# print(list1)

"""6) clear() ---> Removes all elements"""
# l = [1,2,3,4,5]
# l.clear()
# print(l)

"""7) index() ---> Returns index of first occurrence"""
# l = [1,2,3,4,44,4]
# a= l.index(4)
# print(a)

"""8) count()--> Counts how many times value appears"""
# l = [11111,11,1,1,1, 2,3,4]
# print(l.count(1))

"""9) sort() --> Sorts the list (ascending by default)"""
# l = [11,2,22,3,11,223,1,9]
# l.sort()
# l.sort(reverse=True)
# print(l)

"""10. reverse()--> Reverses the list"""
# l = [1,2,3,4]
# l.reverse()
# print(l)

"""11. copy() --> Creates a copy of list"""
# l1 = [1,2,3,4]
# l2 = l1.copy()
# print(l2)
"""------------------------------------------------------------------------"""

"""Dictionary (HashMap) - > dictionary is a data structure they store data in key and value pair and dictionary are mutable """
# Har value ek key ke through access hoti hai
# Keys unique hoti hain
# Values duplicate ho sakti hain

# d = {
#     "name": "Laxit",
#     "age": 21,
#     "city": "Indore"
# }
# print(d)
"""print using loop"""
# for i in d:
#     print(d[i])
"""Add value in list """
# d["marks"] = 89 
# print(d)
"""Update"""
# d["age"] = 20
# print(d)
"""Delete"""
# del d["city"]
# print(d)

"""---------Method of Dictionary------------ """


# d = {"name" : "laxit","age" : 20}

"""1. get()-> Safely value access karne ke liye (error nahi deta)"""
# print(d.get("age"))
# print(d.get("city")) #Jab key exist kare ya na kare, dono handle karna ho

"""2. keys()-> Sabhi keys return karta hai"""
# print(d.keys()) # Sirf keys pe loop chalana ho

"""3. values()-> Sabhi values return karta hai"""
# print(d.values()) 

"""4. items() -> Key + Value pair return karta hai"""
# print(d.items())

# for k, v in d.items():
#     print(k,v)

"""5. update() -> Dictionary ko update ya merge karta hai"""
# d.update({"age": 22, "city": "Indore"})
# print(d)

"""6. pop() -> Specific key remove karta hai"""
# d.pop("age")
# print(d)

"""7.popitem() ->Last inserted item remove karta hai (Python 3.7+)"""
# d.popitem()
# print(d)

"""8. clear() -> Pura dictionary empty kar deta hai"""
# d.clear()
# print(d)

"""copy()-> Dictionary ka shallow copy banata hai"""
# d1 = {"a": 1, "b": 2}
# d2 = d1.copy()

# d2["a"] = 100
# print(d1)  # original change nahi hota

