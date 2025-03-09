# 1. Class with different types of constructors
 class Example:
     def __init__(self, arg1=None, arg2=None):
         if arg1 is None and arg2 is None:
             print("Default constructor called")
         elif arg2 is None:
             print(f"One-argument constructor called with arg1: {arg1}")
         else:
             print(f"Two-argument constructor called with arg1: {arg1}, arg2: {arg2}")
 
 # 2. Calling superclass constructors from a child class
 class Parent:
     def __init__(self, name):
         print(f"Parent constructor called with name: {name}")
 
 class Child(Parent):
     def __init__(self, name, age):
         super().__init__(name)  # Calling superclass constructor
         print(f"Child constructor called with age: {age}")
 
 # 3. Access Modifiers in Constructor
 class Demo:
     def __init__(self):
         print("Public constructor called")
     
     def _protected_constructor(self):
         print("Protected constructor called")
     
     def __private_constructor(self):
         print("Private constructor called")
 
 # 4. Illustrating Attributes of a Constructor
 class Person:
     def __init__(self, name, age):
         self.name = name  # Attribute assignment
         self.age = age
 
     def display(self):
         print(f"Name: {self.name}, Age: {self.age}")
 
 # Testing all the implementations
 print("---- Example Class ----")
 obj1 = Example()
 obj2 = Example(10)
 obj3 = Example(10, 20)
 
 print("\n---- Child Class Constructor Calling Superclass ----")
 child_obj = Child("Surya Sai Krishna", 20)
 
 print("\n---- Access Modifiers in Constructor ----")
 demo_obj = Demo()
 demo_obj._protected_constructor()  # Can be accessed but not recommended
 # demo_obj.__private_constructor()  # This will raise an error
 demo_obj._Demo__private_constructor()  # Accessing private method using name mangling
 
 print("\n---- Attributes in Constructor ----")
 person = Person("Surya Sai Krishna", 21)
 person.display()
