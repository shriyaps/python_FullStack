# Understanding class creation

class Student:
    '''This is a static class of student'''

    # The below block defines attributes of students
    def __init__(self):
        self.name = 'Shriya'
        self.age = 25
        self.marks = 900
        
    # The below block defines a method
    def talk(self):
        print('Hi, I am ', self.name)
        print('My age is ', self.age)
        print('My marks are ', self.marks)

a = Student()
abc = Student()

a.talk()

# Memory location assigned to Student object
print(id(a))
print()

# Memory location assigned to a.talk() object
print('Id of a.talk(): ', id(a.talk))

# To print the variables and its memory locations
print(a.name)
print(id(a.name))
print()

print(a.age)
print(id(a.age))

print()

print(a.marks)
print(id(a.marks))
        
    
