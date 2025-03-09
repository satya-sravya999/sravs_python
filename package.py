# Simulating a package structure in a single file
 
 # Defining ClassOne
 class ClassOne:
     def __init__(self):
         print("Constructor of ClassOne is called.")
 
     def method_one(self):
         print("Method of ClassOne is called.")
 
 # Defining ClassTwo
 class ClassTwo:
     def __init__(self):
         print("Constructor of ClassTwo is called.")
 
     def method_two(self):
         print("Method of ClassTwo is called.")
 
 # Simulating importing classes from a package
 class my_package:
     ClassOne = ClassOne
     ClassTwo = ClassTwo
 
 # Main execution
 if __name__ == "__main__":
     obj1 = my_package.ClassOne()  # Creating an instance of ClassOne
     obj1.method_one()
 
     obj2 = my_package.ClassTwo()  # Creating an instance of ClassTwo
     obj2.method_two()
