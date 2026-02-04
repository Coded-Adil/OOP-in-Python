# Association

# Student, Laptop classes are independent of each other. They can exist without each other.

class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_var = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a {self.laptop_var.brand} laptop.")

laptop1 = Laptop("Dell")
student1 = Student("Alice", laptop1)

student1.show_laptop_info()


# Aggregation
# A class can exist without the other, but one class can have a reference to the other.
# Weak relationship between classes.

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [dept.name for dept in self.departments]
    
uni1 = University("Tech University")
dept1 = Department("Computer Science")
dept2 = Department("Mathematics")
uni1.add_department(dept1)
uni1.add_department(dept2)
print(uni1.show_departments())

# Composition
# Strong relationship between classes. One class cannot exist without the other.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower) # Car creates and owns the Engine. 

    def show_details(self):
        print(f"{self.brand} car with {self.engine.horsepower} HP engine.")

car1 = Car("Toyota", 150)
car1.show_details()