# Class named Car and some objects of that class

# Car -> Brand, Model

class Car:
    def __init__ (self): # self indicates the object itself
        self.brand = ""
        self.model = ""

car1 = Car() # Creating an object of the class Car
car1.brand = "Toyota"
car1.model = "Corolla"

print(car1.brand)
print(car1.model)

car2 = Car()
car2.brand = "Honda"
car2.model = "Civic"

print(car2.brand, car2.model)