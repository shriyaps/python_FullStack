# Python provides a open() function that accepts two arguments,
# file name and access mode in which the file is accessed.

# file_obj = open(fileName,accessMode)

# opens the file akbar_birbal.txt in read mode
file_obj = open("Akbar_birbal.txt",'r')
print(dir(file_obj))
print(file_obj)

print('file opened successfully')

file_obj.close()
