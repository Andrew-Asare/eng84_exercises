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
#task2
menu_food = ["Fried rice", "Fries", "Hot dog", "Salad"]
menu_price = ["3.00", '2.00', '5.00', '3.70']
users_food = []
i = 0
while i < len(menu_food):
    print(menu_food[i].ljust(15) + "£"+menu_price[i])
    i += 1
for i in range(3):
    order = input("What would you like to order? ")
    if order in menu_food:
        users_food.append(order)
    else:
        print("Your order in not valid, please order something else")
print("Here is your order", users_food)










#Task 3


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


#task 4
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






#task 5
























