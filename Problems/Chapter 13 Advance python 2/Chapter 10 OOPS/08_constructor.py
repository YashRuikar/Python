class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):     # __init__ automatically runs the print line. It is called as constructor
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")  

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}") 

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morining, Sir")

    @staticmethod
    def time():
        print("This time is 9AM in the morning")

yash = Employee("Yash", 100000, "YouTube")
# yash = Employee() --> This line throws an error (missing 3 required postional arguments)
yash.getDetails()