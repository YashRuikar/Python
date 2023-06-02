list = ["HARRY", "Harry", "harry", "HaRRy", "haRRy", "HArry","HARry"]
name = input("Enter the name to check\n")
if name in list:
    print("They are talking about harry")
else:
    print("They are not talking about harry")