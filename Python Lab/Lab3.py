# LAB : 3
# 10 Dec, 24
"""
Performed all the Practicals of Set 1
"""

# PRACTICAL : 
# Set 1 => Practical 3.
# A program that generates a random password of a specified lenght.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(length))