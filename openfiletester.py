file = open('document.txt', 'r')
#file = open('testdoc.txt', 'w+')
print "Name of the file: " + file.name

# Reading file
print(file.read() + " \n")
file.close()

# Taking input and writing it to file
file = open('document.txt', 'w+')
input = raw_input("Enter input here: ")
print("writing \'" + input  + "\'")
file.write(input)

# Reading file again
print(file.read())

# Close opend file
file.close()