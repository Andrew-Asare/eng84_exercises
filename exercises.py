#Program calculate year of birth!

# Task 1



#Create a program that calculates the year of birth of a user
import datetime

# Get the current year
current_year = datetime.datetime.now().year
# Get the user to enter age
age = int(input("What is your age"))
# Get the user to enter name
name = input("What is your name?")

# calculate the rough year of birth
year = current_year - age

# Concatinate
print(f"OMG {name}, you are {age} years old so you were born in {year}")

qu = input("Have you had your birthday this year?(Y/N)")
qu = qu.upper() #Make the input uppercase

if qu == "N":
    year = year - 1
    print(year)
    print("This is your real date of birth, sorry for the error")
else:
    print("Have a nice life")







