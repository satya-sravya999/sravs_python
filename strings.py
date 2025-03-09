class StaticExample:
     # Define a static variable
     static_var = 10
 
     @classmethod
     def access_through_class(cls):
         print("Accessing through class:", cls.static_var)
 
     def access_through_instance(self):
         print("Accessing through instance:", self.static_var)
 
     def change_within_instance(self):
         StaticExample.static_var += 5
         print("Changed within instance:", self.static_var)
 
     @classmethod
     def change_within_class(cls):
         cls.static_var += 10
         print("Changed within class:", cls.static_var)
 
 # Access through class
 StaticExample.access_through_class()
 
 # Create an instance
 obj1 = StaticExample()
 obj1.access_through_instance()
 
 # Change within instance
 obj1.change_within_instance()
 StaticExample.access_through_class()  # Observe change
 
 # Change within class
 StaticExample.change_within_class()
 StaticExample.access_through_class()  # Observe change
