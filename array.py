# 1. Function to add integer values of an array
 def sum_of_array(arr):
     return sum(arr)
 
 # 2. Function to calculate the average value of an array of integers
 def average_of_array(arr):
     return sum(arr) / len(arr) if arr else 0
 
 # 3. Program to find the index of an array element
 def find_index(arr, value):
     return arr.index(value) if value in arr else -1
 
 # 4. Function to test if an array contains a specific value
 def contains_value(arr, value):
     return value in arr
 
 # 5. Function to remove a specific element from an array
 def remove_element(arr, value):
     return [x for x in arr if x != value]
 
 # 6. Function to copy an array to another array
 def copy_array(arr):
     return arr.copy()
 
 # 7. Function to insert an element at a specific position in the array
 def insert_element(arr, index, value):
     arr.insert(index, value)
     return arr
 
 # 8. Function to find the minimum and maximum value of an array
 def min_max(arr):
     return (min(arr), max(arr)) if arr else (None, None)
 
 # 9. Function to reverse an array of integer values
 def reverse_array(arr):
     return arr[::-1]
 
 # 10. Function to find the duplicate values of an array
 def find_duplicates(arr):
     return list(set([x for x in arr if arr.count(x) > 1]))
 
 # 11. Program to find the common values between two arrays
 def common_values(arr1, arr2):
     return list(set(arr1) & set(arr2))
 
 # 12. Method to remove duplicate elements from an array
 def remove_duplicates(arr):
     return list(set(arr))
 
 # 13 & 14. Method to find the second largest number in an array
 def second_largest(arr):
     unique_sorted = sorted(set(arr), reverse=True)
     return unique_sorted[1] if len(unique_sorted) > 1 else None
 
 # 15. Method to find number of even and odd numbers in an array
 def count_even_odd(arr):
     evens = len([x for x in arr if x % 2 == 0])
     odds = len(arr) - evens
     return (evens, odds)
 
 # 16. Function to get the difference of largest and smallest value
 def diff_max_min(arr):
     return max(arr) - min(arr) if arr else 0
 
 # 17. Method to verify if the array contains two specified elements (12, 23)
 def contains_elements(arr, elem1=12, elem2=23):
     return elem1 in arr and elem2 in arr
 
 # 18. Program to remove the duplicate elements and return the new array
 def remove_duplicates_new(arr):
     return list(dict.fromkeys(arr))  # Keeps order
 
 # Example usage:
 arr = [10, 20, 30, 20, 10, 40, 50, 60, 10]
 arr2 = [30, 50, 70, 90]
 
 print("Sum:", sum_of_array(arr))
 print("Average:", average_of_array(arr))
 print("Index of 30:", find_index(arr, 30))
 print("Contains 40?", contains_value(arr, 40))
 print("Remove 20:", remove_element(arr, 20))
 print("Copied Array:", copy_array(arr))
 print("Insert 99 at index 2:", insert_element(arr.copy(), 2, 99))
 print("Min and Max:", min_max(arr))
 print("Reversed:", reverse_array(arr))
 print("Duplicates:", find_duplicates(arr))
 print("Common Values:", common_values(arr, arr2))
 print("Remove Duplicates:", remove_duplicates(arr))
 print("Second Largest:", second_largest(arr))
 print("Even & Odd count:", count_even_odd(arr))
 print("Difference between max and min:", diff_max_min(arr))
 print("Contains 12 and 23?", contains_elements(arr))
 print("Remove duplicates (Ordered):", remove_duplicates_new(arr))
