# 1. Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.
# 2. Intermediate: Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
# 3. Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
# 4. Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.


# 1

print('Alternative one.')
student_info = {  
    'name': 'Apio Faith',  
    'age': 20,  
    'grade': 'One'  
}  

for key, value in student_info.items():  #items() recieves all key value pairs from the dictionary, as a tuple(key, value).
    # Th for loop iterates throught the tuple and assigns each  key a key to key and value to a value.
    print(f"{key} ; {value}") #print automatically adds a new line...items() doesn't allow parameters.


print('Alternative two.(List Comprehension.)')
student_info = {  
    'name': 'Apio Faith',  
    'age': 20,  
    'grade': 'One'  
}  

lines = [f'{key}: {value}' for key, value in student_info.items()]
print('\n'.join(lines)) #join() is for concatenating or joining strings.


# 2

def get_adult_names(age_dict):  
    return [name for name, age in age_dict.items() if age >= 21] # List Comprehension.  
#Return defines how the data stored int the function will be manipulated and when to stop.

people_ages = {
    'Alice': 24, 
    'Bob': 19, 
    'Charlie': 30
    }
  
adult_names = get_adult_names(people_ages)  
print(adult_names)  

print('Alternatively, without the use of List Comprehension.')
def get_adult_names(age_dict):  
    adult_names = []  # Create an empty list to store adult names  
    for name, age in age_dict.items():  # Loop through each name-age pair  
        if age >= 21:  # Check if the age is 21 or older  
            adult_names.append(name)  # Add the name to the list if the condition is met  
    return adult_names  # Return the list of adult names  

people_ages = {'Alice': 24, 'Bob': 19, 'Charlie': 30}  
adult_names = get_adult_names(people_ages)  
print(adult_names) 


# 3

prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}  
items_bought = ['apple', 'orange', 'banana', 'banana']  

total_cost = sum(prices[item] for item in items_bought) #List comprehension  
print(f"Total cost: {total_cost}")


# 4

# To count occurances of words and return the result in a dictionary.
def count_word_occurances(sentence):  
    words = sentence.split()  #splits the sentence into words.
    count_dict = {}  # Initializes an empty dictionary to hold the results.
    for word in words:  # loops through each separated word.
        count_dict[word.lower()] = count_dict.get(word, 0) + 1  
#The dict. get() is used to return the value of a key from de dictionary and can take one to two arguments, being the first the key and the second (optional) the value to be returned if the key is not found. If this value is not specified it will return None when key is not found.
#+1 updates the count. .lower() ensures that the words are counted when all are in lower case to prevent counting uppercase and lower case words as two different ones.
    return count_dict  

sentence = "Women studying at women institute of technology."  
print(count_word_occurances(sentence))