# Python program to create a student class with a constructor having more than one parameter

class Student:
    ''' '''
    # This is a constructor
    def __init__(self, n = ' ', m = 0):
        self.name = n
        self.marks = m

    # This is an instance method
    def display(self):
        print('Hi ', self.name)
        print('Your marks: ', self.marks)

# Constructor called without arguements
s = Student(n = 'Shriya', m = 100)
s.display()
print('-------')

def check_input(marks):
    if marks == '':
        marks = 0
    return marks

# Constructor is called with 2 arguments
name = input("Enter your name: ")
marks = check_input(input('Enter your marks: '))

s1 = Student(name, marks)
s1.display()
    
