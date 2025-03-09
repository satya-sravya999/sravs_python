# Step 1: Create a dictionary with initial values
 students = {
     101: "Saladi",
     102: "Satya",
     103: "Sravya",
     
 }
 
 # Step 1.1: Adding new values to the dictionary
 students[106] = "Saladi Satya"
 students[107] = "Satya Sravya"
 
 # Printing the updated dictionary
 print("Updated Student Dictionary:", students)
 # Adding new students to the dictionary
 students[106] = "Saladi Satya"
 students[107] = "Satya Sravya"
 
 # Printing the updated dictionary
 print("Updated Student Dictionary:", students)
 # Updating values in the dictionary
 students[101] = "Saladi Satya Sravya"
 students[102] = "Satya Saladi"
 students[103] = "Sravya Satya"
 
 # Printing the updated dictionary
 print("Dictionary after updating values:", students)
 
 # Accessing values using keys
 print("Student with ID 101:", students[101])
 print("Student with ID 102:", students[102])
 print("Student with ID 103:", students[103])
 
 # Using the get() method (prevents errors if the key is not found)
 print("Student with ID 108:", students.get(108, "Not Found"))
 
 # Creating a nested dictionary
 students = {
     101: {"Name": "Saladi Satya Sravya", "Course": "Python"},
     102: {"Name": "Satya Saladi", "Course": "Java"},
     103: {"Name": "Sravya Satya", "Course": "C++"},
     
 }
 
 # Printing the nested dictionary
 print("Nested Student Dictionary:", students)
 
 # Accessing a specific student's details
 print("Details of Student 101:", students[101])
 
 # Accessing a specific attribute (Name) of a student
 print("Name of Student 102:", students[102]["Name"])
 
 # Accessing a specific attribute (Course) of a student
 print("Course of Student 103:", students[103]["Course"])
 
 # Using get() method to avoid errors if the key doesn't exist
 print("Course of Student 106:", students.get(106, {}).get("Course", "Not Found"))
 
 
 # Printing all keys in the dictionary
 print("Student IDs:", students.keys())
 
 # Printing all keys inside the nested dictionary for a specific student
 print("Keys inside Student 101's data:", students[101].keys())
 
 
 # Check if the key exists before deleting
 if 105 in students:
     del students[105]  # Removes student with ID 105
     print("Student 105 deleted successfully.")
 else:
     print("Student 105 not found, skipping deletion.")
 
 # Using pop() safely
 removed_student = students.pop(104, "Not Found")
 
 # Printing the updated dictionary
 print("Updated Student Dictionary after deletion:", students)
 
 # Printing the removed student details
 print("Removed Student 104:", removed_student)
