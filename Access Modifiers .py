 1. Create a class with PRIVATE fields, private method and a main method.
 
 class PrivateDemo:
     def __init__(self):
         self.__private_var = "I am private"
 
     def __private_method(self):
         print("This is a private method.")
 
     def access_private(self):
         print(self.__private_var)  # Accessing private variable
         self.__private_method()    # Calling private method
 
 class SubPrivateDemo(PrivateDemo):
     def try_access_private(self):
         # print(self.__private_var)  # This will raise an AttributeError
         # self.__private_method()    # This will also raise an AttributeError
         print("Cannot access private members from subclass")
 
 # 2. Create a class with PROTECTED fields and methods.
 
 class ProtectedDemo:
     def __init__(self):
         self._protected_var = "I am protected"
 
     def _protected_method(self):
         print("This is a protected method.")
 
 class SubProtectedDemo(ProtectedDemo):
     def access_protected(self):
         print(self._protected_var)  # Accessing protected variable
         self._protected_method()    # Calling protected method
 
 # 3. Create a class with PUBLIC fields and methods.
 
 class PublicDemo:
     def __init__(self):
         self.public_var = "I am public"
 
     def public_method(self):
         print("This is a public method.")
 
 # Main function to demonstrate access modifiers
 if __name__ == "__main__":
     print("### Private Access ###")
     private_obj = PrivateDemo()
     private_obj.access_private()
 
     sub_private_obj = SubPrivateDemo()
     sub_private_obj.try_access_private()
 
     print("\n### Protected Access ###")
     protected_obj = SubProtectedDemo()
     protected_obj.access_protected()
 
     print("\n### Public Access ###")
     public_obj = PublicDemo()
     print(public_obj.public_var)
     public_obj.public_method()
