
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1>num4):
    f1 = num1
else:
    f1 = num4

if (num2>num3):
    f2 = num2
else:
    f2 = num3

if (f1>f2):
    print(f'{f1} is greatest')
else: 
    print(f'{f2} is greatest')


# import numbers
# numbers = []
# for i in range(0, 4):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# print(f'{max(numbers)} is the maximum between 4 numbers')