# Example for creating list

# How to create a list, we create a list with []
a = []
print(type(a))
print('This is an empty list: ', a)


new_list = [1, 2, 25, 53.56, 'ABC', 3+5j] # Creating a list with various datatype

print(new_list) # Printing our variable
print(type(new_list)) # Printing the datatype of the variable

# To check the mutability of list
print(new_list[2])
print(type(new_list[2]))

# Modify the element in the list
new_list[0] = 10000000000
print(new_list)

# Using reverse indexing
print(new_list[-1])
print(new_list[5])
print(new_list[-2])

################################
name = 'Anurag'
print(name[0:3])

print(name[0:2])

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alpha[0:])

print(alpha[0::1])

print(alpha[0::2])

print(alpha[0:10])

print(alpha[0:10:2])

print(alpha[0::5])

print(alpha[10:])

print(alpha[10:15])

print(alpha[10:15:2])
