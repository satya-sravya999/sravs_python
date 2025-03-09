class OverloadExample:
     # 1. Method Overloading with Different Number of Parameters (Same Type)
     def add(self, a, b=None, c=None):
         if b is None and c is None:
             return a
         elif c is None:
             return a + b
         else:
             return a + b + c
 
     # 2. Method Overloading with Different Number of Parameters (Different Data Types)
     def display(self, value):
         if isinstance(value, int):
             print("Integer value:", value)
         elif isinstance(value, float):
             print("Float value:", value)
         elif isinstance(value, str):
             print("String value:", value)
         else:
             print("Unknown type")
 
     # 3. Same Method Name with Same Number of Parameters (Python does not allow this)
     # We can use conditional logic to handle different behaviors
     def multiply(self, x, y):
         if isinstance(x, int) and isinstance(y, int):
             return x * y
         elif isinstance(x, str) and isinstance(y, int):
             return x * y  # String repetition
         else:
             return "Invalid input"
 
 # Creating an object of the class
 obj = OverloadExample()
 
 # Calling methods with different parameters
 print("Addition with 1 parameter:", obj.add(5))
 print("Addition with 2 parameters:", obj.add(5, 10))
 print("Addition with 3 parameters:", obj.add(5, 10, 15))
 
 # Calling method with different data types
 obj.display(10)
 obj.display(10.5)
 obj.display("Hello")
 
 # Calling method with same number of parameters but different behavior
 print("Multiplication of two integers:", obj.multiply(5, 3))
 print("String repetition:", obj.multiply("Hello ", 3))
