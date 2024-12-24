# Class 6: 24 Dec, 2024
# ABSTRACTION

# from abc import ABC

# class Student(ABC):
#     #class body
#     pass


from abc import ABC, abstractmethod  #abstractmethod ->  Decorator
class Student(ABC):
    @abstractmethod
    def get_name(self):              # abstract method as it does not have any body
        pass


# SUb-class overwriting get_name method
class boy(Student):
    def get_name(self):
        return "Manish"
# Crating object of subclass
obj1=boy()
print(boy.get_name(Student))
