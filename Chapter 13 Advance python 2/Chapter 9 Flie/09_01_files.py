# Use open function to read the content of a file!

#f = open('sample.txt', 'r')
f = open('sample.txt') # By default the mode is r
#text = f.read()
text = f.read(5)  # Reads first 5 characters from the file 
print(text)
f.close()