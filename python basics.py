# 1. Program to print your name
 print("Saladi satya sravya")
 
 # 2. Program for single-line and multi-line comments
 
 # This is a single-line comment
 
 """
 This is a multi-line comment
 It spans multiple lines
 """
 
 # 3. Define variables for different Data Types and print them
 integer_var = 10
 boolean_var = True
 char_var = 'A'  # Python doesn't have a separate char type, so we use a string with one character
 float_var = 10.5
 double_var = 20.123456789  # In Python, float is equivalent to double in other languages
 
 print("Integer:", integer_var)
 print("Boolean:", boolean_var)
 print("Character:", char_var)
 print("Float:", float_var)
 print("Double:", double_var)
 
 # 4. Local and Global variables with the same name
 global_var = "I am global"
 
 def my_function():
     global_var = "I am local"
     print("Inside function:", global_var)  # This refers to the local variable
 
 my_function()
 print("Outside function:", global_var)  # This refers to the global variable
