# Understanding how to split and join strings

# main_string.split(patter)


main_string = 'one,two three,four@Five$Six'
sub_string = main_string.split('$')
print(sub_string)


main_string2 = 'one two three four'
sub_string2 = main_string2.split()
print(sub_string2)


# .split() means splitting based on spaces in the input.
list_colors = input('Enter colors with space: ').split()
print(list_colors)
# Joining of the string
# seperator.join(string)

joined_string = '-'.join(list_colors)
print(joined_string)
