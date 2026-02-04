class Employee:
    company_name = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # Property decorator will have the same name as the 'private' variable    
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
    
obj1 = Employee("John", 50000)

print(obj1.salary)
obj1.salary = 60000
print(obj1.salary)