class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 500

    @property         # getter decorator
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, value):
        self.salaryBonus = value - self.salary

e = Employee()
print(e.totalSalary)

e.totalSalry = 5800
print(e.salary)
print(e.salaryBonus)