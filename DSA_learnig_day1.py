
# How to reverse the order
n=5873

num = n
result =[]

result.append(num % 10 )
while num > 0:

    num = num //10
    remainder = num % 10
    if remainder > 0:
        result.append(remainder)

print(result)


# how to count the digits

num = n
count= 0

while num > 0:
    count += 1
    num = num // 10

print(f'cout of number is {count}')



# Reverseing the number

num = n

result = 0

while num>0:
    remainder = num % 10
    num =num //10
    result = result *10 + remainder
print(f"reverse order is {result}")


# Checking for Armstrong NUmber

"""
153 = 1**3 + 5**3 + 3**3 = 153 then ,yes its a palindrome

"""

num = 153

"""
TO check palindrome condition we need  count of total number and digit of number 
"""

"""
To get the seperate digits 
"""

digits= []

while num > 0:
    remainder = num % 10
    num = num // 10
    digits.append(remainder)

print(f'digits {digits}')

"""
Now to get the counts 
"""
num =153
digit_counts=0

while num >0:
    digit_counts +=1
    num = num // 10

print(f'digit_counts {digit_counts}')


"""
Now its time to check the condition of Amstrong Number 
"""
num = 153
resultant= 0
for i in digits:
    resultant += i ** (digit_counts)
print(resultant)

if resultant == num:
    print(f"Yes the given number is Amstrong number {num} and {resultant}")
else:
    print(f"No, not an Amstrong number {resultant} ")


print("#################Check for Divisors################")
"""
check for Divisors 
10 is divisor with 1,2,5,10 
"""

number = 12
divisors= []
for i in range(1,number+1):
    q= number % i
    if q==0:
        divisors.append(i)
    else:
        pass
print(f"divisors for given numbers are {divisors} ")

"""
Or most optimized way
"""
from math import *
num = 36
divisors = []
for i in range(1,int(sqrt(num)+1)):
    if num % i == 0:
        divisors.append(i)
        if i != num // i:
            divisors.append(num//i)
print(f"divisors= {divisors}")

print(" ########################## Starting Hatch Maapping #############")

"""
Frequency Map 
"""

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,6,2,5,6,7,8,7,3,12,13,16,11,11,14]

item_count_mappering = {}

for item in list:
    if item in item_count_mappering:
        item_count_mappering[item] += 1
    else:
        item_count_mappering[item] = 1
print(item_count_mappering)


print("#################Using Hash-Map#################")

list=list

hash_map = {}
n=len(list)

for i in range(0,n):
    hash_map[list[i]] = hash_map.get(list[i],0) + 1
print(hash_map)


