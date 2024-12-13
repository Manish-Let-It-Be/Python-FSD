# [CLASS] : 13 Dec, 24
# OOPs Concept

'''
Any object have two aspects: 
1. Properties
2. Behaviour


Class: A class is a blueprint for creating objects. It defines the properties and behaviours that objects of that class will have.
Object: An object is an instance of a class. It represents a specific entity with its own set of properties and behaviours.
Example:
Car
Properties: color, model, year, price
Behaviour: start, stop, accelerate, brake

Class: Car
Object: Toyota Camry, Honda Civic, BMW X5, Audi A4

# Structure of Class in Python

class className:
    #body of class
'''
# Example

# class animal:
#     sound = "Bark"

# dog = animal()
# print(dog.sound)  # Output: Bark
# dog.sound = "Woof"
# print(dog.sound)  # Output: Woof
'''
# Constructor in Python

__init__ is a special method in Python that is automatically called when an object is created from a class. It is used to initialize the attributes of the object.
Example:
class animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

dog = animal("Dog", "Bark")
print(dog.name)  # Output: Dog
print(dog.sound)  # Output: Bark

'''
# Write a program to create a class "Student" with properties like Name, Emial, Program, ID, etc.
# where the ID should be generated automatically while creating the object and Student programs should contain list of programs.
# Ask User to enter the data and create the Object and display the Data through Functions.

## APPROACH 1 ##

# class Student:
#     current_id = 1
    
#     def __init__(self, name, email, program):
#         self.name = name
#         self.email = email
#         self.program = program
#         self.id = Student.current_id
#         Student.current_id += 1
#         if Student.current_id > 100: 
#             Student.current_id = 1
    
#     def display_info(self):
#         print("\nStudent Details:")
#         print(f"ID: {self.id}")
#         print(f"Name: {self.name}")
#         print(f"Email: {self.email}")
#         print(f"Program: {self.program}")

# def get_student_input():
#     name = input("Enter student name: ")
#     email = input("Enter student email: ")
#     program = input("Enter student program: ")
#     return name, email, program


# print("Student Registration")
# print("-" * 20)


# name, email, program = get_student_input()
# student = Student(name, email, program)

# student.display_info()

## APPROACH 2 ##

class student:
    name = ""
    email = ""
    program = ""
    stuid = ""

    def display(self):
        print("\nStudent Details:")
        print(f"ID: {self.stuid}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Program: {self.program}")

import random
student1 = student()
student1.name = input("Enter Name: ")
student1.email = input("Enter Email: ")
student1.program = input("Enter Program: ")
student1.stuid = str(random.randint(1, 100))

student1.display()

    