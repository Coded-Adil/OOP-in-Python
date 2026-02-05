# Single Inheritance will allow a child class to inherit properties and methods from a 
# single parent class, while multiple inheritance allows a child class to inherit from 
# multiple parent classes. Multilevel inheritance allows a child class to inherit from 
# a parent class, which in turn inherits from another parent class.


# Multiple inheritance can lead to ambiguity if both parent classes have methods with 
# the same name. In such cases, Python uses the Method Resolution Order (MRO) to determine 
# which method to call. The MRO follows a specific order (depth-first, left-to-right) to 
# resolve method calls in multiple inheritance scenarios.


# Multilevel inheritance can lead to a situation called the "diamond problem," where a child 
# class inherits from two parent classes that both inherit from a common ancestor. In such 
# cases, Python's MRO helps to resolve the ambiguity by determining the order in which methods 
# are inherited.

# Single Inheritance

# class GrandFather:
#     def __init__(self, color, last_name):
#         self.color = color
#         self.last_name = last_name

# By inheriting GrandFather, Father class gets access to its properties and methods

# class Father(GrandFather): # Inheriting from GrandFather
#     def __init__(self, color, last_name, hobby):
#         super().__init__(color, last_name) # Calling GrandFather's constructor
#         self.hobby = hobby

#     def father_method(self):
#         print("This is a method in Father class.")

# obj1 = GrandFather("White", "John")
# obj2 = Father("White", "John", "Fishing")

# print(obj2.color, obj2.last_name, obj2.hobby)

# Multiple Inheritance
# class GrandMother:
#     def __init__(self, eye_color, first_name):
#         self.eye_color = eye_color
#         self.first_name = first_name

# class Mother(GrandMother):
#     def __init__(self, eye_color, first_name, hobby):
#         super().__init__(eye_color, first_name)
#         self.hobby = hobby

#     def mother_method(self):
#         print("This is a method in Mother class.")

# Multilavel Inheritance && Multiple Inheritance
# class Child(Father, Mother): # Inheriting from both Father and Mother
#     def __init__(self, car, color, last_name, hobby, eye_color, first_name):
#         super().__init__(color, last_name, hobby) # Initializing Father part using super()
#         # Father.__init__(self, "White", "John", "Fishing") # Initializing Father part
#         # Mother.__init__(self, "Blue", "Jane", "Gardening") # Initializing Mother part
#         self.eye_color = eye_color
#         self.first_name = first_name
#         self.car = car

# child_obj = Child("Tesla", "White", "John", "Fishing", "Blue", "Jane")
# child_obj.father_method() # Accessing method from Father class
# child_obj.mother_method() # Accessing method from Mother class
# print(child_obj.car, child_obj.color, child_obj.last_name, child_obj.hobby, child_obj.eye_color, child_obj.first_name)

#-----------------------------------------------
# Hierarchical Inheritance
#-----------------------------------------------


# If same class is inherited by multiple child classes, it is called hierarchical inheritance.
# class Vehicle:
#     def engine_type(self):
#         print("Vehical has an engine.")

# class Car(Vehicle):
#     def num_doors(self):
#         print("Car has 4 doors.")

# class Truck(Vehicle):
#     def load_capacity(self):
#         print("Truck can carry 10 tons.")

# car = Car()
# car.engine_type() # Inherited method from Vehicle
# car.num_doors() # Car's own method
# truck = Truck()
# truck.engine_type()
# truck.load_capacity()


#--------------------------------------------------
# Hybrid Inheritance
#--------------------------------------------------

# Different types of inheritance are combined together to form a hybrid inheritance.

class Shape:
    def area(self):
        print("Calculating area ....")

class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides.")

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectangle(5, 3)
rect.sides() # Inherited method from Polygon
print(rect.area()) # Overridden method from Shape class
rect.area() # Calling the area method of Rectangle class, which overrides the area method of Shape class.