"""-------------Basic Level (1–15)----------"""

"""List me har element ka frequency count karo"""
# l = [1,2,3,3,4,5,6,6]
# freq = {}
# for i in l:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1
# print(freq)        

"""Dictionary me maximum value wali key find karo"""
# d = {'a': 10, 'b': 25, 'c': 15}
# max_key = None
# max_value = float('-inf')

# for key, value in d.items():
#     if value > max_value:
#         max_value = value
#         max_key = key
# print(f"Maximum value wali key: {max_key} and vamue: {max_value}")

"""Dictionary ko key ke basis par sort karo"""

"""Bubble Sort Method"""
# d = {'b': 20, 'a': 10, 'c': 30}

# keys = list(d.keys())
# n = len(keys)

# for i in range(n):
#     for j in range(n-i-1):
#         if keys[j] > keys[j+1]:
#             keys[j],keys[j+1] = keys[j+1],keys[j]

# sorted_dict = {}

# for key in keys:
#     sorted_dict[key] = d[key]

# print(sorted_dict)

"""Selection Sort method """
# d = {'b': 20, 'a': 10, 'c': 30}

# keys = list(d.keys())
# n = len(keys)

# for i in range(n):
#     min_index = i
#     for j in range(i+1,n):
#         if keys[j] < keys[min_index]:
#             min_index = j

#     keys[i],keys[min_index] = keys[min_index],keys[i]

# sorted_dict = {}
# for key in keys:
#     sorted_dict[key] = d[key]

# print(sorted_dict)    

"""Dictionary ko value ke basis par sort karo"""
# d = {'a': 10, 'b': 5, 'c': 20, 'd': 15}


# values = list(d.items())
# n = len(values)

# for i in range(n):
#     for j in range(n-i-1):
#         if values[j][1] > values[j+1][1]:
#             values[j],values[j+1] = values[j+1],values[j]

# sorted_dict = {}
# for key, value in values:
#     sorted_dict[key] = value

# print(sorted_dict)


"""Do dictionaries ko merge karo"""
# d1 = {1:10,2:20,3:30}
# d2 = {3:40,5:50,6:60}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

"""Check karo key exist karti hai ya nahi"""
"""method 1"""
# d = {'a': 10, 'b': 20, 'c': 30}

# if 'b' in d:
#     print("Key exist karti hai")
# else:
#     print("Key exist nahi karti")

"""method 2"""
# d = {'a': 10, 'b': 20, 'c': 30}
# if 'b' in d.keys():
#      print("Key exist karti hai")
# else:
#     print("Key exist nahi karti")   

"""method 3"""
# d = {'a': 10, 'b': 20, 'c': 30}  

# if d.get('d') is not None:
#     print("Key exist karti hai")


"""Dictionary ko reverse karo (value → key)"""
# d = {'a': 1, 'b': 2, 'c': 3}

# reversed_dict = {}

# for key, value in d.items():
#     reversed_dict[value] = key

# print(reversed_dict)

"""Reverse order of dictionary (last → first)"""
# d = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

# items = list(d.items())   

# j = len(items) - 1

# for i in range(len(items)//2):
#     items[i], items[j] = items[j], items[i]
#     j -= 1

# reversed_dict = {}
# for key, value in items:
#     reversed_dict[key] = value

# print(reversed_dict)

"""Duplicate values remove karo Dictionary"""
# d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

# unique_dict = {}
# seen_value = []

# for key,value in d.items():
#     if value not in seen_value:
#         unique_dict[key] = value
#         seen_value.append(value)
# print(unique_dict)        


"""Dictionary me total values ka sum nikalo"""
# d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

# sum = 0

# for value in d.values():
#     sum += value
# print(f"sum of value in dictionary : {sum}")    

"""Sabse chhoti value find karo"""
"""method 1"""
# d = {'a': 10, 'b': 20, 'c': 30}

# # small = d['a'] # Agar 'a' key dictionary me nahi hui → error aayega (KeyError)

# values = list(d.values())
# small = values[0]

# for value in d.values():
#     if value < small:
#         small = value
# print(f"{small}")        

"""method 2"""
# d = {'a': 10, 'b': 20, 'c': 30}

# min_key = None
# min_value = float('inf')

# for key, value in d.items():
#     if value < min_value:
#         min_value = value
#         min_key = key

# print(min_key , min_value)        


"""Dictionary me key count karo"""
# d = {'a': 10, 'b': 20, 'c': 30}

# count_key = 0

# for key in d.keys():
#     count_key +=1
# print(count_key)    

"""Ek list ko dictionary me convert karo (index:value)"""
# l = [10, 20, 30, 40]
# d = {}

# for i in range(len(l)):
#     d[i] = l[i]
# print(d)    

"""Dictionary me even values filter karo"""
# d = {'a': 10, 'b': 20, 'c': 3}

# even = {}

# for key,value in d.items():
#     if value%2==0:
#         even[key] = value
# print(even)        


"""String ke characters ka frequency count"""
# s = "programming"
# freq = {}
# for i in s:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1
# print(freq)             

"""Do dictionaries equal hain ya nahi check karo"""

d1 = {'a': 10, 'b': 20}
d2 = {'b': 20, 'a': 10}

if len(d1) != len(d2):
    print(False)
else:
    is_equle = True
    for key in d1:
        if key  not in  d2 or d1[key] !=d2[key]:
            is_equle = False
            break
    print(is_equle)        