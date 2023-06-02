letter = '''Dear <|NAME|>, 
Greetings from <|COMPANY|>. I am happy to tell you that about your selection
You are selected!
Have a great day ahed!
Thanks and regrads,
Date: <|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
company = input("Enter name of company\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
letter = letter.replace("<|COMPANY|>", company)
print(letter)