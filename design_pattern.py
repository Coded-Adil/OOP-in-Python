# Singleton Design Pattern ->

# class Singleton:
#     _instance = None # class variable

#     def __new__(cls): # __new__ is a built-in method in python
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
    
# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2) # Should print True since both s1 and s2 refer to the same instance of Singleton class

#----------------------------------------------------------------------------
# Factory Design Pattern ->
#----------------------------------------------------------------------------

# class Car:
#     def driver(self):
#         return "Driving a car"
    
# class Bike:
#     def driver(self):
#         return "Riding a bike"
    
# class VehicleFactory:
#     @staticmethod
#     def get_vehicle(vehicle_type):
#         if vehicle_type == "car":
#             return Car()
#         elif vehicle_type == "bike":
#             return Bike()
#         else:
#             raise ValueError("Unknown vehicle type")
        
# vehicle = VehicleFactory.get_vehicle("car")
# print(vehicle.driver()) # Should print "Driving a car"


#----------------------------------------------------------------------------
# Builder Design Pattern ->
#----------------------------------------------------------------------------

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}"

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self 

    def set_ram(self, ram):
        self.ram = ram
        return self
    
    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage)
    
builder = ComputerBuilder()
builder.set_cpu("Raizen 3")
builder.set_ram("16GB")
builder.set_storage("512GB SSD")
computer = builder.build()
print(computer) # Should print the details of the computer built using the builder pattern