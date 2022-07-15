# Understanding the counting of sub string we use count() method

# main_string.count(substring)

# main_string.count(substring, beginning, end)


main_string = input('Enter main string: ')
sub_string = input('Enter sub string: ')
print(len(main_string))

num = main_string.count(sub_string, 328, -290)
print(num)


# count() method using starting and ending

main_string = input('Enter main string: ')
sub_string = input('Enter sub string: ')
print(len(main_string))

num = main_string.count(sub_string, 0, 74)
print(num)
