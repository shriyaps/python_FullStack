# Local Variable in a function
def myfunction():
    a = 1           # This is a local variable
    a += 1          # Increment it
    print("This is 'a' inside the function: ", a)       # Display 2

# Calling myfunction()
myfunction()
# print(a)        # Error, not available




# Global Variable in a function
a = 1               # This is global variable
def myfunction():
    b = 2           # This is local variable
    print('Printing value of "a" from within the function = ', a)   # Display Global Variable)
    print('b inside function = ', b)        # Display local variable

myfunction()

print('Outside function a: ', a)    # Available
# print(b)    # Error, not available




# Same name for Global and Local Variable
a = 11          # This is global variable
def myfunction():
    a = 2       # This is local variable
    print('Inside function a = ', a)        # Display local variable

myfunction()
print('Outside function a = ', a)



# The GLOBAL KEYWORD
# Program to access the global variable inside a function
# And modify it

a = 10      # This is global variable
print('This is first a: ', a)

def myfunction():
    global a    # This is global variable
    print('Global a: ', a)
    a = 2       # Modify global variable value
    print('Modified a = ', a)       # Display new value

myfunction()
print('Global a: ', a)      # Display modified value



# Same name for Global and Local Variable
a = 10              # This is global variable
def myfunction():
    a = 2           # a is local variable
    x = globals()['a']   # Get global variable into x)
    print('Global variable a as x: ', x)
    print('Local variable a: ', a)

myfunction()
print('Global variable a: ', a)
    




































    
    
    
    

          
