import os
 
 file_path = r"C:\Users\sai\Desktop\python_ass\sample.txt.txt"
 
 # 1. Program to read a text file
 def read_text_file():
     try:
         with open(file_path, "r") as file:
             content = file.read()
             print("File Content:\n", content)
     except FileNotFoundError:
         print("Error: File not found!")
     except Exception as e:
         print("An error occurred:", e)
 
 # 2. Program to write text to a .txt file
 def write_text_file():
     try:
         with open(file_path, "w") as file:
             file.write("Hello, this is a sample text file.\nThis is a test write operation.")
         print("Text written to file successfully!")
     except Exception as e:
         print("An error occurred while writing:", e)
 
 # 3. Program to read a file stream
 def read_file_stream():
     try:
         with open(file_path, "r") as file:
             for line in file:
                 print(line.strip())  # Reading line by line
     except FileNotFoundError:
         print("Error: File not found!")
 
 # 4. Program to read a file stream with random access
 def read_random_access():
     try:
         with open(file_path, "r") as file:
             file.seek(10)  # Move cursor to 10th byte
             print("Random Access Read:", file.read(20))  # Read next 20 bytes
     except FileNotFoundError:
         print("Error: File not found!")
 
 # 5. Program to read a file at a particular index using seek()
 def read_at_index(index):
     try:
         with open(file_path, "r") as file:
             file.seek(index)  # Move cursor to given index
             print("Data from index", index, ":", file.read(10))  # Read next 10 characters
     except FileNotFoundError:
         print("Error: File not found!")
 
 # 6. Program to check file read and write permissions
 def check_file_permissions():
     if os.path.exists(file_path):
         print("Read Permission:", os.access(file_path, os.R_OK))
         print("Write Permission:", os.access(file_path, os.W_OK))
     else:
         print("File does not exist.")
 
 # Calling the functions
 write_text_file()  # Write to file first
 read_text_file()
 read_file_stream()
 read_random_access()
 read_at_index(5)
 check_file_permissions()
