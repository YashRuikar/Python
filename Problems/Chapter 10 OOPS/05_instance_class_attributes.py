class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
print(harry.salary)
print(rajni.salary)

# Creating instance attribute company for both the objects
# harry.company = "FaceBook"
# rajni.comapany = "TCS"
print(harry.company)
print(rajni.company)

# Below line throws an error as address is not present in instance/class
# print(rajni.address)