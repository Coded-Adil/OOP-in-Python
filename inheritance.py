# Single Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

# By inheriting GrandFather, Father class gets access to its properties and methods

class Father(GrandFather): # Inheriting from GrandFather
    def __init__(self, color, first_name, hobby):
        super().__init__(color, first_name) # Calling GrandFather's constructor
        self.hobby = hobby

obj1 = GrandFather("White", "John")
obj2 = Father("White", "John", "Fishing")

print(obj2.color, obj2.first_name, obj2.hobby)