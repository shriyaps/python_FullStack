# Python OS module enables interaction with the operating system
import os

# 1. Renaming a file
os.rename('00000000000000.txt', 'python_write_example.txt')

# 2. Deleting a file
os.remove('To be deleted.txt')

# 3. Creating the new directory
os.mkdir('New Directory')

# 4. To get the current working dictionary
path = os.getcwd()
print(path)

# 5. To remove a dictionary
os.rmdir('New Directory')
