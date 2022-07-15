# Types of variables in classes

# 1. Instance Variables
# 2. Class Variables or Static Variables

# instance var example
class Sample:
    '''This is a simple example instance variable'''
    # This is a constructor
    def __init__(self):
        self.x = 10     # This is an instance variable

    # This is an instance method
    def modify(self):
        self.x += 1

a = Sample()
# xyz = Sample()
print(a.x)
a.modify()
print(a.x)
xyz = Sample()
print(xyz.x)

# Create 2 instance
s1 = Sample()
s2 = Sample()

s1.modify()
s1.modify()
s1.modify()
print('x in s1: ', s1.x)
print('x in s2: ', s2.x)


# Class Variables or Static Variables example

# class vars or static variables example
class Sample:
    # This is a class var or static var
    x = 10

    # this is a class method
    @classmethod
    def modify(cls):
        cls.x += 1

# Create 2 instance
s1 = Sample()
s2 = Sample()

print('x in s1 = ', s1.x)
print('x in s2 = ', s2.x)

# Modify x in s1 only
s1.modify()
s1.modify()
s1.modify()

print('x in s1 = ', s1.x)
print('x in s2 = ', s2.x)

