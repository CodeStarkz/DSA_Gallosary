import random

list_1 = [random.randint(1,10) for i in range(101)]

list_2 = [random.randint(1,10) for i in range(11)]

"""
now we have to check how many elements of list_1 are present in list_2 and how many times
"""

# as we have information that list_2 have values between 1 to 10
list_holder = [0]
hash_list = list_holder * 11

for item in list_2:
    hash_list[item] += 1

print(f"count of elements of list _2 stored at hash_list[element] value, {hash_list} ")
print(list_2)

"""
Now lets count the number of elements of list_1 present in list_2
"""
value_count_list = [0]* 11
for item in list_1:
    value_count_list[item] += 1

print(f"value stored at index is representing the repetetion of no of times of element present in list_1, {value_count_list}")
print(list_1)
