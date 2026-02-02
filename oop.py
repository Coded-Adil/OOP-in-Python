# Class named Car and some objects of that class

# 3 Types of Constructors:
# 1. Default Constructor -> No parameters
# 2. Parameterized Constructor -> With parameters
# 3. Default Values Constructor -> With default values for parameters

# Car -> Brand, Model


# If a functin is inside a class, it is called a method
class Car:
    # Constructor -> __init__ -> Dunder method -> No return type
    # def __init__ (self): # self indicates the object itself # This is a default constructor
    #     self.brand = ""
    #     self.model = ""

    # def __init__(self, brand="", model=""): # Parameterized constructor
    #     self.brand = brand
    #     self.model = model

    def __init__ (self, brand = "Honda", model = "Civic"): # Default values constructor
        self.brand = brand
        self.model = model
    
    def display_info(self): # Instance method
        print(f"Car Brand: {self.brand} \nCar Model: {self.model}")

car1 = Car("Toyota", "Corolla") # Creating an object of the class Car
# car1.brand = "Toyota"
# car1.model = "Corolla"

# print(car1.brand)
# print(car1.model)

car2 = Car()
# car2.brand = "Honda"
# car2.model = "Civic"

# print(car2.brand, car2.model)

car1.display_info()
car2.display_info()