# To read a file method using the Python script, the python provides
# the read() method.

# open file with 'r' mode
with open('Akbar_birbal.txt', 'r') as f:
    content = f.read()
    print(content)
    print()
    print(type(content))

# open file with 'r' mode
with open('Akbar_birbal.txt', 'r') as f:
    content = f.read(25)
    print(content)
    print()
    print(type(content))
