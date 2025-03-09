def arithmetic_operations(a, b):
     print(f"Addition: {a + b}")
     print(f"Subtraction: {a - b}")
     print(f"Multiplication: {a * b}")
     print(f"Division: {a / b if b != 0 else 'Cannot divide by zero'}")
 
 def increment_decrement(num):
     print(f"Original Number: {num}")
     num += 1
     print(f"After Increment: {num}")
     num -= 1
     print(f"After Decrement: {num}")
 
 def check_equality(x, y):
     if x == y:
         print("The numbers are equal.")
     else:
         print("The numbers are not equal.")
 
 def relational_operators(x, y):
     print(f"{x} < {y}: {x < y}")
     print(f"{x} <= {y}: {x <= y}")
     print(f"{x} > {y}: {x > y}")
     print(f"{x} >= {y}: {x >= y}")
 
 def print_smaller_larger(x, y):
     smaller = min(x, y)
     larger = max(x, y)
     print(f"Smaller number: {smaller}")
     print(f"Larger number: {larger}")
 
 # Example usage:
 a, b = 10, 5
 arithmetic_operations(a, b)
 increment_decrement(a)
 check_equality(a, b)
 relational_operators(a, b)
 print_smaller_larger(a, b)
