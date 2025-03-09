import os
 
 # 1. Generate Arithmetic Exception Without Exception Handling
 def arithmetic_exception():
     num1 = 10
     num2 = 0
     result = num1 / num2  # This will cause ZeroDivisionError
     print("Result:", result)
 
 # 2. Handle the Arithmetic Exception Using Try-Except Block
 def handle_arithmetic_exception():
     try:
         num1 = 10
         num2 = 0
         result = num1 / num2  # This will cause ZeroDivisionError
         print("Result:", result)
     except ZeroDivisionError:
         print("Error: Cannot divide by zero!")
 
 # 3. Method That Throws Exception and Call It Without Try Block
 def throw_exception():
     num1 = 10
     num2 = 0
     return num1 / num2  # This will cause ZeroDivisionError
 
 # 4. Multiple Catch Blocks (Handling Different Exceptions)
 def multiple_catch_blocks():
     try:
         num1 = int(input("Enter a number: "))
         num2 = int(input("Enter another number: "))
         result = num1 / num2
         print("Result:", result)
     except ZeroDivisionError:
         print("Error: Cannot divide by zero!")
     except ValueError:
         print("Error: Invalid input! Please enter numbers only.")
     except Exception as e:
         print("An unexpected error occurred:", e)
 
 # 5. Throw Exception with Custom Message
 def throw_custom_exception():
     raise Exception("This is a custom exception message!")
 
 # 6. Create a Custom Exception
 class CustomError(Exception):
     def __init__(self, message):
         super().__init__(message)
 
 def create_custom_exception():
     raise CustomError("This is my own exception!")
 
 # 7. Program with Finally Block
 def finally_block_example():
     try:
         print("Trying to divide numbers...")
         result = 10 / 2
         print("Result:", result)
     except ZeroDivisionError:
         print("Error: Cannot divide by zero!")
     finally:
         print("This will always execute, whether an exception occurs or not.")
 
 # 8. Generate Arithmetic Exception
 def generate_arithmetic_exception():
     return 10 / 0  # ZeroDivisionError
 
 # 9. Generate FileNotFoundException
 def generate_file_not_found_exception():
     with open("non_existent_file.txt", "r") as file:
         data = file.read()
 
 # 10. Generate ClassNotFoundException (Not applicable in Python, using ImportError)
 def generate_class_not_found_exception():
     import non_existent_module  # This will cause ImportError
 
 # 11. Generate IOException (Handled as OSError in Python)
 def generate_io_exception():
     try:
         os.remove("non_existent_file.txt")  # Attempting to delete a non-existing file
     except OSError as e:
         print("IO Error:", e)
 
 # 12. Generate NoSuchFieldException (Handled as AttributeError in Python)
 class SampleClass:
     def __init__(self):
         self.exists = "I am here"
 
 def generate_no_such_field_exception():
     obj = SampleClass()
     print(obj.non_existent_field)  # AttributeError
 
 # Running the functions to demonstrate exception handling
 if __name__ == "__main__":
     print("1. Arithmetic Exception Without Handling")
     try:
         arithmetic_exception()
     except ZeroDivisionError:
         print("Error occurred (as expected).")
 
     print("\n2. Handling Arithmetic Exception")
     handle_arithmetic_exception()
 
     print("\n3. Throw Exception Without Handling")
     try:
         throw_exception()
     except ZeroDivisionError:
         print("Error: Cannot divide by zero!")
 
     print("\n4. Multiple Catch Blocks")
     multiple_catch_blocks()
 
     print("\n5. Throw Custom Exception")
     try:
         throw_custom_exception()
     except Exception as e:
         print("Caught Exception:", e)
 
     print("\n6. Create and Raise Custom Exception")
     try:
         create_custom_exception()
     except CustomError as e:
         print("Caught Custom Exception:", e)
 
     print("\n7. Finally Block Example")
     finally_block_example()
 
     print("\n8. Generate Arithmetic Exception")
     try:
         generate_arithmetic_exception()
     except ZeroDivisionError:
         print("Error: Cannot divide by zero!")
 
     print("\n9. Generate FileNotFoundException")
     try:
         generate_file_not_found_exception()
     except FileNotFoundError:
         print("Error: File not found!")
 
     print("\n10. Generate ClassNotFoundException (ImportError in Python)")
     try:
         generate_class_not_found_exception()
     except ImportError:
         print("Error: Module not found!")
 
     print("\n11. Generate IOException")
     generate_io_exception()
 
     print("\n12. Generate NoSuchFieldException")
     try:
         generate_no_such_field_exception()
     except AttributeError:
         print("Error: No such field exists!")
