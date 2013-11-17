# Open a file

file = open('document.txt', 'r+')
print "Name of the file: ", file.name

str = file.read()
print(str + " \n")

input = raw_input("Enter input here: ")
print("writing \" " + input  + " \"")
file.write(input)

str = file.read()
print(str)

# Close opend file
file.close()