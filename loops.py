# 1
#Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop
print("Even numbers between 1 and 20.")
for even_numbers in range(2,21,2):
    print(even_numbers)
# It's like printing the values in this range.


print('Using an alternative method.')
#Alternative two
for even_number in range(1,21):
    if even_number % 2 == 0:
        print(even_number)



# 2
# Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.

# Initiating the loop with a number less than 10.
number = 0

while number <= 10:
    # A while loop is a function that continues a process until a condition is met. 
    number = int(input('Enter any number. And a number greater than 10 to stop: '))
    if number <= 10:
        print('Enter another number and a number greater than 10 to stop: ')
    else:
        print("You've entered a number greater than 10. Exiting loop")


# 3
#  Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.

print('The multiples [from 1 to 10] of numbers 1 to 5.')
for numbers in range(1,6):
    for multiple in range(1,11):
        print(f"{numbers} x {multiple} = {number * multiple}")

    
# 4
# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.

integers = [4, 7, 2, 9, 12, 15]
odd_sum = 0

for odd_numbers in integers:
    if odd_numbers %2 != 0:
        odd_sum += odd_numbers

print(f"The sum of odd number in the list of integers is: {odd_sum}")

print("Alternatively")
odd_summation = sum( odd_number for odd_number in integers if odd_number %2 != 0)
print(f"The sum of odd number in the list of integers is: {odd_summation}")