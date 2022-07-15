# Returning results from a function

# Function to add two numbers
def sum(a, b):
    '''This function will add two numbers'''
    c = a + b
    return c

# call the function

a = sum(100, 50)
print(a)

# Example 1
if a >= 100:
    a -= 100
    print(a)

# Example 2
x = sum(10, 20)
multiply = x*10

print("This is x: ", x)
print("This is multiply: ", multiply)
