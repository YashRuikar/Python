class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.Salary}")

harry = Employee()
harry.Salary = 100000
harry.getSalary()   # Employee.getSalary(harry)