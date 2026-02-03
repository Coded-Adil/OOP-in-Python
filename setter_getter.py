class Employee:
    company_name = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        # By convention, prefixing with an underscore to indicate 'private' variable But still accessible
        self._salary = salary # Private variable

    def get_salary(self, password):
        if password == "admin123":
            print(f"Access Granted to {self.name} Salary: {self._salary}")
        else:
            print("Access Denied: Incorrect Password")
    
    def set_salary(self, new_salary, password):
        if password == "admin123":
            self._salary = new_salary
            print(f"Salary updated to {new_salary} for employee {self.name}")
        else:
            print("Access Denied: Incorrect Password")

    
emp1 = Employee("John", 50000)
emp2 = Employee("Harry", 60000)

emp1.get_salary("123")  # Incorrect password
print(emp1._salary)  # Direct access (not recommended)

emp2.get_salary("admin123")  # Correct password
print(emp2._salary)  # Direct access (not recommended)

emp1.set_salary(55000, "wrongpass")  # Incorrect password
emp1.set_salary(55000, "admin123")  # Correct password