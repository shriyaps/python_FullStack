# Understanding the startswith 

# main_string.startswith(sub_string)
name = input('Enter your name: ')
sub_string = input('Enter the sub_string: ')
# n = name.startswith(sub_string)
# print(n)

if name.startswith(sub_string):
    print('Yes')
else:
    print('No')



# Understanding the endswith
# main_string.endswith(sub_string)

name2 = input('Enter your name: ')
sub_string2 = input('Enter the sub_string: ')

if name2.endswith(sub_string2):
    print('Yes')
else:
    print('No')
