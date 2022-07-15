# An exception example
# An exception is a runtime error which can be handled by the programmer. That means if the
# programmer can guess an error in the program and he can do something to eliminate the harm
# caused by that error, then it is called an 'exception'. If the programmer cannot do anything
# in case of an error, then it is called an 'error' and not an exception.

a, b = [int(x) for x in input('Enter two space seperated numbers, Division by 0 is not allowed: ').split()]

c = a/b
print('The division is: ', c)
