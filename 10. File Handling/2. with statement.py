# The 'with' statement is useful in the case of manipulating the files.

# with open(filename, accessmode) as filePointer

with open('Akbar_birbal.txt', 'r') as f:
    content = f.read()
    print(content)
    
          
