# Superclass A
 class A:
     def __init__(self):
         self.value = "Value from Class A"
 
     def method1(self):
         print("Method1 from Class A")
 
     def method2(self):
         print("Method2 from Class A")
 
     def common_method(self):
         print("Overridden method in Class A")
 
 
 # Subclass B (Inheriting from A)
 class B(A):
     def __init__(self):
         super().__init__()
         self.value = "Value from Class B"
 
     def method3(self):
         print("Method3 from Class B")
 
     def method4(self):
         print("Method4 from Class B")
 
     def common_method(self):
         print("Overridden method in Class B")
 
 
 # Subclass C (Inheriting from B)
 class C(B):
     def __init__(self):
         super().__init__()
         self.value = "Value from Class C"
 
     def method5(self):
         print("Method5 from Class C")
 
     def method6(self):
         print("Method6 from Class C")
 
     def common_method(self):
         print("Overridden method in Class C")
 
 
 # Main class
 if __name__ == "__main__":
     # Creating objects for each class
     a = A()
     b = B()
     c = C()
 
     # Calling all methods using their own objects
     print("\nMethods from Class A:")
     a.method1()
     a.method2()
     a.common_method()
 
     print("\nMethods from Class B:")
     b.method3()
     b.method4()
     b.common_method()
 
     print("\nMethods from Class C:")
     c.method5()
     c.method6()
     c.common_method()
 
     # Demonstrating runtime polymorphism
     print("\nCalling overridden method using superclass reference:")
     ref = B()
     ref.common_method()  # Calls common_method from B
 
     ref = C()
     ref.common_method()  # Calls common_method from C
 
     # Demonstrating runtime polymorphism with instance variables
     print("\nRuntime Polymorphism with Data Members:")
     ref = A()
     print(ref.value)
 
     ref = B()
     print(ref.value)
 
     ref = C()
     print(ref.value)
