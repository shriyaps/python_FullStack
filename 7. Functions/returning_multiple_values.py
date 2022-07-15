# Returning Multiple Values from a Function

def sum_sub(a, b):
    '''doc string'''
    c = a + b
    d = a - b
    z = a * b
    return c, d, z

# Calling function
p,q,r = sum_sub(10, 20)
print(p,q,r, sep = ',')

# Defining variables
a = 50
b = 100

# p,q,r = sum_sub(a, b)
# print(p,q,r, sep = ',')

# This will give the tuple with 2 elements
x = sum_sub(a, b)
print(x)
