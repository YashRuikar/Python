# n! = (n-1)! * n
# sum(n) = sum(n-1) + n

def recurSum(n):
    if n <= 1:
        return n
    else:
        return n + recurSum(n-1)

print(recurSum(5))
