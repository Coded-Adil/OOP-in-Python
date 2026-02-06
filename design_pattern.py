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

class Car:
    def driver(self):
        return "Driving a car"
    
class Bike:
    def driver(self):
        return "Riding a bike"
    
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")
        
vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.driver()) # Should print "Driving a car"