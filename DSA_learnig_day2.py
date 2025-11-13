"""
DSA Learning Day2
"""

print("############################### Frequency Counter#############################")

import random as rd

number_collections= [rd.randint(1,20) for i in range(100)]

print(number_collections)

frequency_map = {}
length = len(number_collections)

for i in range(0,length):
    frequency_map[number_collections[i]] = frequency_map.get(number_collections[i],0) + 1
print(frequency_map)

print("############## Problem 2 ############## Hashing ########## ")
"""
Check item of list 
"""
m= list(rd.randint(1,19)for i in range(500))
n=list(rd.randint(1,20)for i in range(30))
mapper ={}

for item in m:
    if item in n:
        print(f"item {item} is present in both list")
        mapper[item] = mapper.get(item,0) + 1
    else:
        print(f"item {item} is not present in both list")
print(mapper)




