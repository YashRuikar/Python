def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good")

a = increment('df34')
print(a)