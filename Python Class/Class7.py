# Clas : 7
# Date : 27 Dec, 2024

# Method Overoloading

# class Sum:
#     def add(self, a, b, c=0):
#         return a + b + c

# sum_instance = Sum()

# result_two = sum_instance.add(5, 10)
# print(f"Sum of two numbers (5 + 10): {result_two}")  # Outputs: 15

# result_three = sum_instance.add(5, 10, 15)
# print(f"Sum of three numbers (5 + 10 + 15): {result_three}")  # Outputs: 30


# # Method Overriding

# class Animal:
#     def speak(self):
#         return "Animal sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog = Dog()
# cat = Cat()

# # Call the overridden method
# print(f"Dog: {dog.speak()}")  # Outputs: Dog: Woof!
# print(f"Cat: {cat.speak()}")  # Outputs: Cat: Meow!



# Sir's example:
class a:
    def show(self):
        print("Showing Parent class")
class b(a):
    def show(self):
        print("Showing Child class")

obj1=a()
obj2=b()
obj1.show()
obj2.show()