# LAB : 1 
# 26 Nov, 24

# Intro to Python Lang


'''
Python
    [ Guido van Rossum ] began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0
        Features:
        > High Level Lang
        > Object Oriented Programming Lang
        > Interpreted Language
        > Dynamic Typing
        > Easy to Learn
'''



# print("HEllo World")
# print("Ramanujan Number: ", 1729)
# print("Type of 1729: ", type(1729))
# print("Type of Hello World: ",type("Hello World"))
# number = 1729
# print("Number plus one: ", number+1)
# print("\n\n\n\n")


# stringVariable = "Hello World"
# print("String variable:",stringVariable)
# intVariable = 1729
# print("Int Variable:",intVariable)
# print("Type Casting: " + stringVariable + " " + str(intVariable))



import calendar

# Print the calendar for a specific month
year = 2024
month = 12
print(calendar.month(year, month))

# Print the full calendar for the year
print(calendar.calendar(year))



from tqdm import tqdm
import time

# Example: Progress bar for a loop
for i in tqdm(range(20)):
    time.sleep(0.1)  # Simulate some work
    
    

import pyjokes

# Get a random joke
joke = pyjokes.get_joke()
print("Random Joke:", joke)

from termcolor import colored

# Print colored text
print(colored("Hello, world!", "red"))
print(colored("Success!", "green"))
print(colored("Error!", "yellow", "on_red"))


