# Understanding how to calculate the string length

a = 'This is the seventh chapter in python basic courses.'
print(len(a))

b = 'Hello World'
print(len(b))

# range(start, stop-1, step)

for i in range(0, len(b)):
    print('hello')

name = input('Enter your name: ')
if len(name) <= 5:
    print("Change your name")
else:
    print("Yeaah..")
