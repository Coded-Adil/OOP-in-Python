# Singleton Design Pattern ->

class Singleton:
    _instance = None # class variable

    def __new__(cls): # __new__ is a built-in method in python
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # Should print True since both s1 and s2 refer to the same instance of Singleton class