class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer): # Which class is written first prority is given to first class inside the bracket of programmer class
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)