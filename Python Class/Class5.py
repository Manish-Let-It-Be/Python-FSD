# class demo:
#     def __init__(self, name, email, phone):
#         self.name = name     #publoc
#         self._email = email   # protected
#         self.__phone = phone  # private



# Write a program to create a Encapsulated class of Library and display their details after creating the objects.

class library:
    def __init__(self, name=None, address=None, books=None):
        self.__name = name 
        self.__address = address
        self.__books = books
    
    #Getter method for name property
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_books(self):
        return self.__books
    #Setter method for name property
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_books(self, books):
        self.__books = books

obj1 = library()
obj1.set_name("Manish")
obj1.set_address("Kathmandu")
obj1.set_books("Python")
print(obj1.get_name())
print(obj1.get_address())
print(obj1.get_books())
