# Poly -> Multipul
# Morphism -> Form
# Polymorphism -> Many Forms

# 2 types of polymorphism
# Method Overriding -> When a child class provides a specific implementation of a method that is already defined in its parent class, it is called method overriding. The child class's method will be called instead of the parent class's method when invoked on an instance of the child class.

class GrandFather:
    def greet(self):
        print("GrandFather says")

class Father(GrandFather):
    def greet(self):
        print("Father says")

class Child(Father):
    def greet(self):
        print("Child says")

grand_father = GrandFather()
father = Father()
child = Child()

grand_father.greet() # Calls GrandFather's greet method
father.greet() # Calls Father's greet method
child.greet() # Calls Child's greet method

# Method Overloading -> Method overloading is a feature that allows a class to have multiple methods with the same name but different parameters. However, Python does not support method overloading in the traditional sense as seen in other programming languages. Instead, you can achieve similar functionality using default arguments or variable-length arguments.

class Shape:
    def area(self, a, b = 10):
        return a * b
    
p = Shape()
print(p.area(5)) 
print(p.area(5, 20)) 