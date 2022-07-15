##### Example of sets in python
##
### Creating set with repeated values
my_set = {1, 2, 2, 2, 2, 2, 2, 2, 1, 5, 5.5, 5.1, 2, 'Hello', '125', 'Happy', '125'}
print("This is my set: ", my_set)

### This will give the error, as indexing is not supported in set
## my_set[0] = 25
##
print("This is the type of set: ", type(my_set)) # Printing the datatype
##
# Adding an individual element in set
my_set.add(55)
my_set.add("This is the example")
print(my_set) # Printing the variable
#
# Removing an element from set
my_set.remove("Hello")
print(my_set)
print(type(my_set))

# 1. Starts with curly brackets.
# 2. No repetation of elements in set.
# 3. Randomly arranged elements at output.
