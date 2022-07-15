# Anonymous Functions or Lambdas

# lambda variables:expression


x = 5
y = 5
z = x + y
print(z)

def sum(x, y):
    z = x + y
    print(z)

sum(5, 5)

# Lambda function to calculate sum of the values
f = lambda x, y, z: (x + y)*z
value = f(5, 5, 2)
print('Calculation of values is: ', value)


# Lambda function to calculate multiplication of the values
f = lambda x, y, z: x * y * z
value = f(5, 5, 10)
print('Calculation of values is: ', value)


# Lambda function to find the bigger number
maxx = lambda x, y: x if x > y else y
a, b = [int(n) for n in input('Enter two numbers: ').split()]
print('Bigger number is: ', maxx(a, b))

#########################################################################

# Using lambdas with filter() function
# filter(function, sequence)

# Using filter() function put the even numbers from a list
def is_even(x):
    '''To check if if the value is even number'''
    if x % 2 == 0:
        return True
    else:
        return False

# Let us take a list of numbers
lst = [10, 20, 30, 40, 55, 77, 68279, 638814, 5281, 3541, 543185]

# Call the filter() with is_even and lst
lst1 = list(filter(is_even, lst))
print(lst1)

lst1 = list(filter(lambda x : True if x % 2 == 0 else False, lst))
print(lst1)

##########################################################################

# map() function
# map(function, sequence)

# map() function that gives square
def square(x):
    '''To get square'''
    return x*x

# Let us take a list of numbers
lst = [146, 3154, 6148, 61834, 611, 4, 10]

# Call mapp() function with square() and lst
lst1 = list(map(square, lst))
print(lst1)

lst1 = list(map(lambda x : x*x, lst))
print(lst1)

############################################################################

# reduce() function
# reduce(function, sequence)
from functools import *
lst = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x*y, lst)
print(result)




































































































