# To write some text to a file, we need to open the file using the open
# method with one of the following access mode

# w: overwrite the file if any exists
# a: append the existing file. The file pointer is at end of the file.
    # It creates a new file if no file exists.


# open file with 'w' mode
with open('python_write_example.txt', 'w') as f:
    f.write('''Python is the modern day language. It is used for web development.''')

# open file with 'a' mode
with open('python_write_example.txt', 'a') as f:
    f.write(''' This line will append to the existing file''')
