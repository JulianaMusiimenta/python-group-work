#1. Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.
#2. Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
#3. Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.
#4. Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).


# 1

class Car:  
    def __init__(self, brand, color):  
        self.brand = brand  
        self.color = color  

my_car = Car('Mercedes Benz', 'Matte Black')  
print(f"Brand: {my_car.brand}, Color: {my_car.color}")


# 2 

class Car:  
    def __init__(self, brand, color):  
        self.brand = brand  
        self.color = color  

    def start_engine(self):  
        print(f"The engine of the {self.color} {self.brand} has started.")

my_car = Car('Mercedes Benz', 'Matte Black')  
print(f"Brand: {my_car.brand}, Color: {my_car.color}")

#self is crucial in OOP for:
#Referring to the instance of a class.
#Accessing instance attributes and methods.
#Allowing each instance of a class to maintain its own state.


# 3 

class BankAccount:  
    def __init__(self, account_number, balance):  
        self.account_number = account_number  
        self.balance = 0  

    def deposit(self, amount): 
        # Deposit an amount into the account. 
        self.balance += amount  
        print(f"Deposited: {amount}")  

    def withdraw(self, amount):
        # Withdraw an available amount from the account.  
        if amount <= self.balance:  
            self.balance -= amount  
            print(f"Withdrew: {amount}")  
        else:  
            print("Insufficient balance!")  

    def print_balance(self):  
        #Print the current account balance.
        print(f"Account Balance: {self.balance}")  


# 4

# Library management system
class Library:  
    def __init__(self):  
        self.books = []  # A list to store books as dictionaries  

    def add_book(self, title, author):  
        """Add a new book to the library."""  
        book = {  
            'title': title,  
            'author': author,  
            'available': True  # Initially, the book is available  
        }  
        self.books.append(book)  
        print(f"Added: {book}")  

    def remove_book(self, title):  
        """Remove a book from the library by title."""  
        for book in self.books:  
            if book['title'] == title:  
                self.books.remove(book)  
                print(f"Removed: {book}")  
                return  
        print(f"Book titled '{title}' not found.")  

    def find_book(self, title):  
        """Find a book by title."""  
        for book in self.books:  
            if book['title'] == title:  
                return book  
        return None  

    def borrow_book(self, title):  
        """Borrow a book, marking it as unavailable."""  
        book = self.find_book(title)  
        if book and book['available']:  
            book['available'] = False  
            print(f"Checked out: {book}")  
        else:  
            print("Book is either not found or is already checked out.")  

    def return_book(self, title):  
        """Return a book, marking it as available."""  
        book = self.find_book(title)  
        if book:  
            book['available'] = True  
            print(f"Returned: {book}")  
        else:  
            print("Book not found.")  

    
