# Class Variable will stay same for all instances/objects of the class
# Instance Variable will be different for each instance/object of the class

class School:
    school_name = "Greenwood High"  # Class variable

    def __init__(self, name):
        self.student_name = name  # Instance variable

sc1 = School("Alice")
sc2 = School("Bob")

sc1.school_name = "Sunrise Academy"  # Modifying class variable via instance
# School.school_name = "Sunrise Academy"  # Correct way to modify class variable

print(sc1.school_name)  # Accessing class variable via instance
print(sc1.student_name)  # Accessing instance variable via instance
print(sc2.school_name, sc2.student_name)  