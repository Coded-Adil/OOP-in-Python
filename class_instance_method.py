class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self): # Instance method
        print(f"Employee Name: {self.name}, Salary: {self.salary}, Company: {self.company_name}")

    @classmethod
    def change_company_name(cls, name): # Class method
        cls.company_name = name

emp1 = Employee("John", 50000)
emp2 = Employee("Harry", 60000)
emp1.display_info()

# emp1.change_company_name("InnoTech") # This would raise an error since change_company_name is a class method
Employee.change_company_name("InnoTech")
print(f"Company Name: {Employee.company_name}")
print(f"Company Name from emp1: {emp1.company_name}")
print(f"Company Name from emp2: {emp2.company_name}")