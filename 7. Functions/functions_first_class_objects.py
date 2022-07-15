# Functions are First Class Objects

# It is possible to assign a function to a variable
# It is possible to define one function inside another function
# It is possible to pass a function as parameter to another function
# It is possible that a function can return another function


# Assign a function to a variable
def display(str):
    return 'Hi! ' + str

x = display('Shriya')
print(x)


# Define a function inside another function
def display(str):
    def message():
        return 'How are you '
    result = message() + str + ' ?'
    return result

print(display('Shriya'))
print(15*'-----')


# Functions can be passed as parameters to other functions
def addition(fun):
    c = 10 + fun
    return c

def number():
    return 100
    return 'How are you?'

print(addition(number()))
print()
print(15*'----')


# Function can return another function
def addition():
    def multiplication():
        print("This is multiplication")
        return 10*20

    def movie():
        print("This is a movie name")
        return 'Superman'

    return multiplication, movie

a, b = addition()
print(b())
print()
