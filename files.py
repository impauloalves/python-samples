# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Mode: ', myFile.mode)

# Write to file
myFile.write('I love popcorns')
myFile.write(' and Python')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like dogs.')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
