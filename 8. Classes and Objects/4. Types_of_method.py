# Types of methods

# 1. Instance Method
#           (a) Accessor Method
#           (b) Mutator Method

# 2. Class Method

# 3. Static Method

# instance method to process data of the objects
class Student:
    ''''''
    # This is a constructor
    def __init__(self, n = ' ', m = 0):
        self.name = n       # Instance Variable
        self.marks = m      # Instance Variable

    # This is an instance method, and accessor method
    def display(self):
        print('Hi my name is: ', self.name)
        print('My marks are: ', self.marks)

    # To calculate grades based on marks is also an instance method
    # This is mutator method
    def calculate(self):
        if(self.marks >= 600):
            print('You got first grade')
        elif(self.marks >= 500):
            print('You got second grade')
        elif(self.marks >= 350):
            print('You got third grade')
        else:
            print('Better luck next time!')

# Create instance with some data from keyboard
# n = int(input("How many students? ")
# i = 0
# while (i < n):

name = input('Enter name: ')
marks = int(input('Enter marks: '))

# Create Student class instance and store data
s = Student(name, marks)
s.display()
s.calculate()
# i += 1
print(10*'------')


# Python program to use class method to handle common feature of all instance

# Understanding class methods
class Bird:
    ''' '''
    # This is a class var
    wings = 2

    # This is a class method
    @classmethod
    def fly(clas, name):
        print(f'{name} flies with {Bird.wings} wings')
#       print('{} flies with {} wings'.format(name, cls.wings))

# Display information for 2 birds
Bird.fly('Sparrow')
Bird.fly('Pigeon')
print(10*'------')

# Python program to create static method that counts the number of instances

# Understanding static methods
class Myclass:
    ''' '''
    # This is class var or static var
    n = 0

    # COnstructor that increments n when an instance is created
    def __init__(self):
        Myclass.n = Myclass.n+1         # a = a + 1

#   def variable_class(cls):
#       print(cls.n)

    # This is a static method to diplay the no of instances
    @staticmethod
    def noObjects():
        print(f'No. of instances created: {Myclass.n}')

# Create 3 instances
obj1 = Myclass()
Myclass.noObjects()

obj2 = Myclass()
Myclass.noObjects()

obj3 = Myclass()
Myclass.noObjects()


        

        

        
