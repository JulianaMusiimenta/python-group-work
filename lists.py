# 1
# Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.

fruit_list = ['banana', 'orange', 'pineapple', 'watermelon', 'cucumber']
for fruits in fruit_list:
    print(fruits, end='\n') #sep may be used in place of end.

# 2
# Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].

#Use a function and return
numbers = [9, 10, 11 ]

#Creating a list of the squares.
squared_numbers = [ number**2 for number in numbers]
print(squared_numbers)

# 3 
# Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print('Using alternative one.')
print(list1 + list2)

print('Using alternative two.')
for n in list2:
    list1.append(n)
    print(list1)

print('Using alternative three.')
list1.extend(list2)
print(list1)

# 4
# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.

values = [3, 1, 4, 1, 5, 9, 2]

print("Alternative one.")
sorted_list = sorted(values) #Returns a new sorted list.
print(sorted_list)

print(f"The two largest numbers in the list are {sorted_list[-1]} and {sorted_list[-2]}")

print("Alternative two.")
values.sort() # Sorts a list and thus should be used directly.

print(f"The two largest numbers in the list are {values[-1]} and {values[-2]}")



#To get the distinct largest values
#Use a set to get the distinct values
distinct_values = set(values)

#Sort the distinct values
sorted_distinct = sorted(distinct_values)

print(f"The two largest numbers in the list are {values[-1]} and {values[-2]}")

#Or if the distinct values are few.

# Check if we have at least two distinct numbers  
if len(sorted_distinct) >= 2:  
    # Get the two largest distinct numbers  
    largest = sorted_distinct[-1]  
    second_largest = sorted_distinct[-2]  
    print(f"The two largest distinct numbers are {largest} and {second_largest}.")  
else:  
    print("There are not enough distinct numbers to determine two largest values.")  
