# Example on how to create a tuple
# Tuples are immutable

# How to create a tuple
tup = ()

my_tuple = (100, "This is Cognitio", 52.36, 3+2j) # creating a tuple
print(my_tuple) # Printing the variable data
print(type(my_tuple)) # Printing the datatype of variable
print(type(my_tuple[1]))
print(my_tuple[1])

### This will give an error
# my_tuple[0] = 'I am happy'
