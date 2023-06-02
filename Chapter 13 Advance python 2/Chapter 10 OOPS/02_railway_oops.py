class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Phone number is {self.phoneNumber}\n")


yashApplication = RailwayForm()
yashApplication.name = "Yash"
yashApplication.train = "Mahalaxmi Express"
yashApplication.phoneNumber = "9130768054"
yashApplication.printData()


shubhamApplication = RailwayForm()
shubhamApplication.name = "Shubham Ruikar"
shubhamApplication.train = "Rajdhani Express"
shubhamApplication.phoneNumber = "9970173510"
shubhamApplication.printData()