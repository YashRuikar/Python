# n! = 1 x 2 x 3 x 4 x ...... x n
# 5! = 1 x 2 x 3 x 4 x 5



num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")