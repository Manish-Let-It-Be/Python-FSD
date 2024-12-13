# LAB : 3
# 10 Dec, 24
# I was absent
"""
Performed all the Practicals of Set 1
"""

# PRACTICAL : 
# Set 1 => Practical 3.
# AIM : A program that generates a random password of a specified lenght given by user.

# import random
# import string

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password

# length = int(input("Enter the desired password length: "))
# print("Generated password:", generate_password(length))



# PRACTICAL : 
# Set 1 => Practical 4.
# AIM : A program that calculates Average of a list of numbers.

# def avg(num):
#     total = sum(num)
#     average = total / len(num)
#     return average

# user_input = input("Enter numbers separated by spaces: ")

# numbers = list(map(float, user_input.split()))

# average = avg(numbers)
# print("Average: ", average)



# PRACTICAL : 
# Set 1 => Practical 5.
# AIM : A program that checks if the given year is a Leap year.

# def checkLeap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False

# year = int(input("Enter a year: "))

# if checkLeap(year):                            # If checkLeap is True
#     print(f"{year} is a Leap Year.")
# else:
#     print(f"{year} is not a Leap Year.")       # If checkLeap is False




# PRACTICAL : 
# Set 1 => Practical 6.
# AIM : A program that calculates the Factorial of a number.

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact(num - 1)

# num = int(input("Enter a number: "))
# result = fact(num)
# print(f"The factorial of {num} is {result}")


# PRACTICAL : 
# Set 1 => Practical 7.
# AIM : A program that checks if a given string is palindrom

# def isPalindrome(s):
#     s = s.lower()
#     return s == s[::-1]

# s = input("Enter a string: ")
# ans = isPalindrome(s)
# if ans:
#     print(f"Yes, The string [{s}] is a palindrome.")
# else:
#     print(f"No, The string [{s}] is not a palindrome.")

'''
NOTE 
s[::-1] is a slicing operation that reverses the string s.
The slice syntax [start:stop:step] works as follows:
  > start: Where to begin slicing (default is the start of the string).
  > stop: Where to stop slicing (default is the end of the string).
  > step: The step size. A negative step (-1) means traverse the string in reverse.
Example:
s = "hello"
reversed_s = s[::-1]  # "olleh"

'''


# PRACTICAL : 
# Set 1 => Practical 8.
# AIM : A program that sorts a list of numbers in Ascending or Descending Order.

## APPROACH 1 ##
# elements = int(input("Enter the number of elements: "))
# lst = []
# for i in range(elements):
#     num = int(input("Enter a number: "))
#     lst.append(num)
# print(f"Original List: {lst}")
# lst.sort()
# print(f"Sorted List in Ascending Order: {lst}")
# lst.sort(reverse=True)
# print(f"Sorted List in Descending Order: {lst}")


## APPROACH 2 ##
# def sort(numbers, order):
#     if order.lower() == "asc":
#         return sorted(numbers)                                      # sorted(iterables, key=len, reverse=True/False)
#     elif order.lower() == "dsc":
#         return sorted(numbers, reverse=True)
#     else:
#         raise ValueError("Order must be 'asc' or 'dsc'.")

# try:
#     user_input = input("Enter numbers separated by spaces: ")
#     numbers = list(map(float, user_input.split()))  
#     order = input("Enter the sorting order (asc/dsc): ")

    
#     sorted_numbers = sort(numbers, order)
#     print(f"Sorted numbers in {order.lower()} order: {sorted_numbers}")
# except ValueError as e:
#     print(f"Error: {e}")


# PRACTICAL : 
# Set 1 => Practical 9.
# AIM : A program that generate a Multiplication Table for a given number.

# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")
    


# PRACTICAL : 
# Set 1 => Practical 10.
# AIM : A program that converts a given number from one base to another.

## APPROACH 1 ##
# n = int(input("Enter a decimal number: "))

# binary = bin(n)
# print(f"Binary: {binary}")

# hexadecimal = hex(n)
# print(f"Hexadecimal: {hexadecimal}")

# octal = oct(n)
# print(f"Octal: {octal}")


## APPROACH 2 ##
# def to_binary(number):
#     return bin(number)[2:]  # `bin` adds '0b' prefix, [2:] removes it

# def to_hexadecimal(number):
#     return hex(number)[2:]  # `hex` adds '0x' prefix, [2:] removes it

# def to_decimal(number, from_base):
#     return int(number, from_base)

# try:
#     number = input("Enter the number to convert: ")
#     from_base = int(input("Enter the base of the number (2/10/16): "))
#     to_base = int(input("Enter the base to convert to (2/10/16): "))

#     decimal_number = to_decimal(number, from_base) if from_base != 10 else int(number)

#     if to_base == 2:
#         result = to_binary(decimal_number)
#     elif to_base == 16:
#         result = to_hexadecimal(decimal_number)
#     elif to_base == 10:
#         result = str(decimal_number)
#     else:
#         raise ValueError("Unsupported base. Use 2, 10, or 16.")

#     print(f"The number {number} in base {from_base} is {result} in base {to_base}.")
# except ValueError as e:
#     print(f"Error: {e}")





# HOMEWORK: Make a Color Game using python.
'''
Instructions ⬇️⬇️

Welcome to the color game>>>
please enter the name for score board

1> start game
2> exit

if 1
please enter the color: redasddfa
 validate the color if the given color is not present in the
 list then tell user you have entered invalid color

 if color is validated then
 match it with machine generated color
 if matching then display the message like
 you wom the game
 number of attempts : 1
 total number of attempts: 5

 if not matching then display the message:

 your guess was wrong please try again
 number of attempts left: 04

 once after completing the game till 5th attempts tell user
 1> see score board
 2> play again
 3> exit

 if he  choose 1 then:
 number of game won:01
 number of game loose:01
 name of the player: abc
  \
"""

'''


import random

# List of valid colors
VALID_COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]

class ColorGame:
    def __init__(self):
        self.games_won = 0
        self.games_lost = 0
        self.player_name = ""
    
    def start_game(self):
        self.player_name = input("Please enter your name for the scoreboard: ").strip()
        while True:
            print("\n1> Start Game")
            print("2> Exit")
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.play_game()
            elif choice == "2":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def play_game(self):
        print("\nStarting the game...")
        machine_color = random.choice(VALID_COLORS)
        attempts = 0
        max_attempts = 5
        
        while attempts < max_attempts:
            attempts += 1
            user_color = input("\nPlease enter a color: ").strip().lower()
            
            if user_color not in VALID_COLORS:
                print("Invalid color. Please enter a valid color.")
                attempts -= 1  # Invalid attempt does not count
                continue
            
            if user_color == machine_color:
                print(f"You won the game! 🎉\nNumber of attempts: {attempts}")
                self.games_won += 1
                break
            else:
                attempts_left = max_attempts - attempts
                if attempts_left > 0:
                    print(f"Your guess was wrong. Please try again. Attempts left: {attempts_left}")
                else:
                    print(f"Sorry, you've used all attempts. The correct color was '{machine_color}'.")
                    self.games_lost += 1
        
        self.post_game_menu()
    
    def post_game_menu(self):
        while True:
            print("\n1> See Scoreboard")
            print("2> Play Again")
            print("3> Exit")
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.display_scoreboard()
            elif choice == "2":
                self.play_game()
                break
            elif choice == "3":
                print("Exiting the game. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")
    
    def display_scoreboard(self):
        print("\n--- Scoreboard ---")
        print(f"Player Name: {self.player_name}")
        print(f"Number of games won: {self.games_won}")
        print(f"Number of games lost: {self.games_lost}")


# Main program
if __name__ == "__main__":
    print("Welcome to the Color Game!")
    game = ColorGame()
    game.start_game()

