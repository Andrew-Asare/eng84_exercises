# #Program calculate year of birth!
#
# # Task 1
#
#
#
# #Create a program that calculates the year of birth of a user
# import datetime
#
# # Get the current year
# current_year = datetime.datetime.now().year
# # Get the user to enter age
# age = int(input("What is your age"))
# # Get the user to enter name
# name = input("What is your name?")
#
# # calculate the rough year of birth
# year = current_year - age
#
# # Concatinate
# print(f"OMG {name}, you are {age} years old so you were born in {year}")
#
# qu = input("Have you had your birthday this year?(Y/N)")
# qu = qu.upper() # Make the input uppercase
#
# if qu == "N":
#     year = year - 1
#     print(year)
#     print("This is your real date of birth, sorry for the error")
# else:
#     print("Have a nice life")
#
#
# task2
# menu_food = ["Fried rice", "Fries", "Hot dog", "Salad"]
# menu_price = ["3.00", '2.00', '5.00', '3.70']
# users_food = []
# i = 0
# while i < len(menu_food):
#     print(menu_food[i].ljust(15) + "£"+menu_price[i])
#     i += 1
# for i in range(3):
#     order = input("What would you like to order? ")
#     if order in menu_food:
#         users_food.append(order)
#     else:
#         print("Your order in not valid, please order something else")
# print("Here is your order", users_food)
#
#


# Task 3


#
# class Fizzbuzz:
#     # init with default values for fizz (3), buzz (5)
#     def __init__(self):
#         self.fizz = 3
#         self.buzz = 5
#
#     # play game with default max number set to 100
#     def words(self):
#                 # loops through numbers from 1 to and including 100 whilst printing what needs to be printed according to the if statment
#         for num in range(1, 101):
#
#             if (num % self.fizz == 0) and (num % self.buzz == 0): # Using modulos to check if the remainder = 0, if this is true then that number is a multiple of the correlating fizzbuzz word
#                 print("FizzBuzz")
#
#             elif num % self.fizz == 0:
#                 print("Fizz")
#
#             elif num % self.buzz == 0:
#                 print("Buzz")
#
#             else:
#                 print(num)
#
#
# if __name__ == "__main__":
#     fizz_buzz = Fizzbuzz()
#     fizz_buzz.words()


# task 4
#
# import random
# import string
#
# class ScrabbleCalc:
#
#     def __init__(self): # A list of all the letters with their values
#         self.letter_vals = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
#                             "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
#                             "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
#                             "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
#                             "y": 4, "z": 10
#                             }
#         self.word = ""
#         self.score = 0
#
#     def calculate_score(self, word):
#         lower = word.lower().strip()
#
#         for char in lower:
#             self.score += self.letter_vals[char]
#
#         print(f"{word} is worth {self.score} points!")
#         self.reset_calc()
#
#     def reset_calc(self):
#         self.word = ""
#         self.score = 0
#
#
# if __name__ == "__main__":
#     string.ascii_letters: 'abcdefghijklmnopqrstuvwxyz'
#     char_set = string.ascii_letters.lower()
#     word = ''.join(random.sample(char_set, random.randint(0, 10))) # random sample returns a paticular legth list of items, random randint chooses a random integer from 0 to 10
#     calc = ScrabbleCalc()
#     calc.calculate_score(word)
#


# # Task 5
# # Simple program to use control flow
#
# age = 19
# driver_lisence = True
#
# # Rules
# # you can vote to drive
# # you can vote
# # you can't leagally drink but your mates/uncles might have your back (bigger 16)
# # Your too young, go back to school!
# # As a user I should be able to keep being prompted for input until I say 'exit'
# #
#
# def get_permission(age, driver_license):
#     # Check if age is number
#     if isinstance(age, str):
#         if age.isdigit():
#             age = int(age)
#
#
#     if age <= 17:
#         print('You are too young to do anything, go back to school')
#
#     #   driving if license == True
#     elif age < 18:
#         if driver_license:
#             print('You can drive')
#         else:
#             print("You still can't drive")
#     # age > 18
#     #   drinking
#     #   voting
#     #   driving if license == True
#     else:
#         if driver_license:
#             print('You can vote and drive')
#         else:
#             print('You can drive')
#
#
# def ask_number():
#     while True:
#         choice = input()
#         if choice.isdigit():
#             choice = int(choice)
#             if num_in_bounds(choice):
#                 return choice
#         print('Oops there was a problem, please try again: ')
#
#
# def num_in_bounds(number):
#     if number > 0:
#         return True
#     return False
#
#
# def yes_no_true_false(value):
#     if value.lower() in ['y', 'yes']:
#         return True
#     elif value.lower() in ['n', 'no']:
#         return False
#     return None
#
#
# def ask_yes_no():
#     while True:
#         choice = yes_no_true_false(input())
#         if choice is not None:
#             return choice
#         print('Bad value')
#
#
# def showcase():
#     print("If i am 12 years old and i have a fake drivers license")
#     get_permission(12, True)
#
#     print('\nIf i am 16 and a half, again with fake license')
#     get_permission(16.5, True)
#
#     print('\nIf i am 17 and a half without a license')
#     get_permission(17.5, False)
#
#     print('\nIf i am 17 and a half and finally got my license')
#     get_permission(17.5, True)
#
#     print('\nWhen i turn 18')
#     get_permission(18, True)
#
#     print('\nIf lose my license at 55')
#     get_permission(55, False)
#
#
# if __name__ == '__main__':
#
#     while True:
#         choice = input("\nCheck your permissions?\n (Enter any value to continue, or enter 'exit' to quit)\n")
#         if choice.lower() == 'exit':
#             break
#         print('What is your age?')
#         age = ask_number()
#         if age >= 17:
#             print('Do you have a license(y/n)?')
#             drivers_license = ask_yes_no()
#             get_permission(age, drivers_license)
#         else:
#             # if driver is less than 17 don't even ask for license
#             get_permission(age, False)
#     print('Goodbye')


# Task 6

# Your going to write a story, cut it into section, store the section in a python dictionary!

#
#
# story = {"start": "Once upon a time there was a dog",
#           "middle": "The dog liked barking at the moon",
#           "end": "in the end it ended up barking at the sun too"
#           }
#
#
# # Print the entire dictionary
#
# for key, val in story.items():
#     print(key + ":", val)
#
# # Print the type of your dictionary
# print("\nPrint the type of your dictionary:")
# print(type(story))
#
# # Print only the keys
# print("\nPrint only the keys:")
# for key in story.keys():
#     print(key)
#
# # Print only the values
# print("\nPrint only the values:")
# for val in story.values():
#     print(val)
#
# # Print the individual values using the keys
# print(story["start"])
# print(story["middle"])
# print(story["end"])
#
# # Now let's add a new key:value pair
# story["hero"] = "Doge"
# print("hero: " + story["hero"])
#


# Task 7
#
# list_names = []  # Used in name_loop and names_lower_loop
# list_names_lower = []  # Used in names_lower_loop
# list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Used in list_values_is_even
#
#
# # For loop using range that prints hello 10 times
# def hello_loop():
#     for _ in range(0, 10, 1):
#         print("Hello")
#
#
# # For loop that asks the user to input 10 names to add to a list
# def name_loop():
#     print("Could you please provide me with a set of 10 names?")
#
#     for num in range(1, 11, 1):  # Loop 10 times and add user input to list_names
#         list_names.append(input(f"Please enter name {num}: "))
#
#     print(f"list_names = {list_names}")  # Print list_names when function ends
#
#
# # For each loop that converts all the names provided by list_names,
# # converts them to lower case and adds them to list_names_lower
# def names_lower_loop():
#     for name in list_names:  # loop through list_names
#         list_names_lower.append(name.lower())  # lower name and add it to list_names_lower
#
#     print(f"list_names_lower = {list_names_lower}")
#
#
# # A simple for each loop that uses modulus to determine if values
# # in a list are even or odd
# def list_values_is_even():
#     for value in list_values:
#         if value % 2 == 0:
#             print(f"{value} is even!")
#             continue
#
#         print(f"{value} is odd!")
#
#
# if __name__ == "__main__":
#     hello_loop()
#     name_loop()
#     names_lower_loop()
#     list_values_is_even()


# # Task 8
# def list():
#
#     return_list = []  # This is the list it will return
#     print("\nHO HO HO! What do you want for Christmas?")
#
#     # This will loop until the word exit forces a break
#     while True:
#         user_input = input()  # get input
#
#         if user_input.lower().count("exit") > 0:  # break if there is 1 or more instances of the word "exit" in the input
#             break
#
#         return_list.append(user_input)  # Add the item to the list
#         print("What else would you like?")
#
#     return return_list
#
#
# # This prints the list in a nice format for the user to read
# def print_list(item_list):
#     print("\nMy Christmas List:")
#     count = 1
#     for item in item_list:  # For each item in the list print it in a nice format with a unique number
#         print(f"{count}. {item.upper()}")
#         count += 1
#
#
# # First generate the list, then print it back to the user
# if __name__ == "__main__":
#     xmas_list = list()
#     print_list(xmas_list)
