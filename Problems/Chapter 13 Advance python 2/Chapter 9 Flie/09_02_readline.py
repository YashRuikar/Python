f = open('sample.txt')
# Read first line
text = f.readline()
print(text)  # Prints only the first line doesn't print the other line

# Read second line
text = f.readline()
print(text)

# Read third line
text = f.readline()
print(text)

# Read fourth line and so on
text = f.readline()
print(text)
f.close()