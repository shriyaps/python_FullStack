# Decorators in functions

def decor(fun):                 # Giftwrapping

    def inner():
        value = fun()           # Access value returned by fun()
        return value + 2        # Increase the value by 2
    return inner

@decor                          # Calling the decorator function
def num():
    return 10

print(num())

##############################################################################

# Call decorator function and pass num and comment the '@decor'
# result_fun = decor(num
# print(result_fun()) # Call result_fun and display the result


# Calling decorator function using '@' method
def decor_two(fun):
    def inner(*args,**kwargs):
        value = fun(*args,**kwargs)           # Access value returned by fun()
        return value + 2        # Increase the value by 2
    return inner                # Return the inner function

# Calling decorator function using '@' method
def decor_eight(fun):
    def inner(*args,**kwargs):
        value = fun(*args,**kwargs)           # Access value returned by fun()
        return value + 8        # Increase the value by 8
    return inner                # Return the inner function

# Take a function to which decorator should be applied
@decor_two
@decor_eight
def num(a,b):
    '''Some statements process'''
    return a+b

# Call decorator function and pass num
print(num(6,7))                    
