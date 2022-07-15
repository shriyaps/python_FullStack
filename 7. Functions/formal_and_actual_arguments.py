# Formal and Actual arguments

# This Actual Arguments used in a function call are of 4 types:
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable Length Arguments

# 1. Positional Arguments
def attach(s1, s2):
    '''to join s1 and s2 and display total string'''
    s3 = s1 + s2
    print(s3)

# Call attach() and pass 2 strings
attach('New ', 'York')
attach('York ', 'New')


# 2. Keyword Arguments
def grocery(product, price):
    '''To display the given arguments'''
    print('Product: ', product)
    print('Price: ', price)

# Call the grocery function and pass 2 arguments
# grocery(100, 'Sugar')
grocery(price = 100, product = 'Sugar')


# 3. Default Arguments
def grocery(product, price = 40.00):
    '''To display the given arguments'''
    print('Product: ', product)
    print('Price: ', price)

# Call the grocery () function and pass arguments
grocery(price = 45.0, product = 'Sugar')
grocery(product = 'Sugar')


# 4. Variable Length Arguments
def add(abc, *args):            # *args can take 0 or more values
    '''To add given numbers'''
    print('Formal Argument: ', abc)

    sum = 0
    for i in args:
        sum += i
    print('Sum of all numbers: ', (abc + sum))

# Calling add() function and pass arguments
# add(5, 10)
add(50, 10, 20, 30, 40, 50)


# 5. Variable Length Argument using Dictionary

def display(farg, **kwargs):
    '''To display given values'''
    print('Formal Argument: ', farg)

    for x, y in kwargs.items():
        print(f'Key = {x}, Value = {y}')

# Calling the function
# display(5, rno = 10)
print()

display(5, rno = 1, name = 'Shriya')

    
