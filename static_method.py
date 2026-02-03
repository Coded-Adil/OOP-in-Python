# Static method looks similar to a normal function defined inside a class.
# Work: Static method organizes functions that have some logical connection with the class.
# Kind of a helper function that belongs to the class.
# No dependency on instance or class variables.

class School:
    school_name = "Greenwood High"  # Class variable

    def __init__(self, name):
        self.student_name = name  # Instance variable

    @staticmethod
    def calculate_grade(marks):  # Static method
        if marks >= 90:
            return 'A'
        elif marks >= 80:
            return 'B'
        elif marks >= 70:
            return 'C'
        elif marks >= 60:
            return 'D'
        else:
            return 'F'
        
print(School.calculate_grade(85))  # Calling static method without creating an instance