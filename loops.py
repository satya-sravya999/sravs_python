# 1. Program to print "Bright IT Career" ten times using for loop
 def print_message():
     for _ in range(10):
         print("Bright IT Career")
 
 # 2. Program to print numbers from 1 to 20 using while loop
 def print_numbers_while():
     i = 1
     while i <= 20:
         print(i, end=" ")
         i += 1
     print()
 
 # 3. Program demonstrating equal and not equal operators
 def compare_numbers(a, b):
     print(f"{a} == {b}: {a == b}")
     print(f"{a} != {b}: {a != b}")
 
 # 4. Program to print odd and even numbers in a range
 def print_odd_even(n):
     print("Even numbers:", [x for x in range(n + 1) if x % 2 == 0])
     print("Odd numbers:", [x for x in range(n + 1) if x % 2 != 0])
 
 # 5. Program to print the largest number among three numbers
 def largest_of_three(a, b, c):
     return max(a, b, c)
 
 # 6. Program to print even numbers between 10 and 20 using while loop
 def print_even_while():
     i = 10
     while i <= 20:
         if i % 2 == 0:
             print(i, end=" ")
         i += 1
     print()
 
 # 7. Program to print numbers from 1 to 10 using do-while loop (simulated)
 def do_while_simulation():
     i = 1
     while True:
         print(i, end=" ")
         i += 1
         if i > 10:
             break
     print()
 
 # 8. Program to check if a number is an Armstrong number
 def is_armstrong(n):
     order = len(str(n))
     return n == sum(int(digit) ** order for digit in str(n))
 
 # 9. Program to check if a number is prime
 def is_prime(n):
     if n < 2:
         return False
     for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
             return False
     return True
 
 # 10. Program to check if a number is a palindrome
 def is_palindrome(n):
     return str(n) == str(n)[::-1]
 
 # 11. Program to check whether a number is EVEN or ODD using a dictionary (switch simulation)
 def even_odd_switch(n):
     switch = {0: "EVEN", 1: "ODD"}
     return switch[n % 2]
 
 # 12. Print gender (Male/Female) based on 'M' or 'F' using a dictionary (switch simulation)
 def gender_switch(g):
     switch = {'M': "Male", 'F': "Female"}
     return switch.get(g.upper(), "Invalid Input")
 
 # Example usage:
 print_message()
 print_numbers_while()
 compare_numbers(5, 10)
 print_odd_even(10)
 print("Largest:", largest_of_three(10, 20, 30))
 print_even_while()
 do_while_simulation()
 print("Is 153 Armstrong?", is_armstrong(153))
 print("Is 17 prime?", is_prime(17))
 print("Is 121 palindrome?", is_palindrome(121))
 print("Number 7 is:", even_odd_switch(7))
 print("Gender for 'M':", gender_switch('M'))
