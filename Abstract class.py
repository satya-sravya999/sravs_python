from abc import ABC, abstractmethod
 
 # 1. Create an abstract class with abstract and non-abstract methods.
 class AbstractDemo(ABC):
     def __init__(self, value):
         self.value = value
     
     @abstractmethod
     def abstract_method(self):
         pass  # Abstract method (must be implemented in child class)
 
     def non_abstract_method(self):
         print(f"Non-abstract method called. Value: {self.value}")
 
 # 2. Create a subclass for an abstract class and access non-abstract methods.
 class ConcreteClass(AbstractDemo):
     def __init__(self, value):
         super().__init__(value)
 
     def abstract_method(self):
         print(f"Abstract method implemented in {self.__class__.__name__}")
 
 # 3. Create an instance for the child class in the child class and call abstract methods.
 # 4. Create an instance for the child class in the child class and call non-abstract methods.
 if __name__ == "__main__":
     obj = ConcreteClass(10)  # Creating an object of the child class
     obj.non_abstract_method()  # Accessing the non-abstract method
     obj.abstract_method() 
