# String testing examples

# To check string is alphabet or not
name = input('Enter the name: ')
if name.isalpha():
    print(name)
else:
    print('No')

# To check string is a digit or not
mobile = input('Enter a mobile number: ')
if mobile.isdigit():
    print(mobile)
else:
    print('No')

# To check string is alphabet and numeric or not
captcha = input('Enter a captcha: ')
if captcha.isalnum():
    print(captcha)
else:
    print('No')

# To check string is upper or not
name = input('Enter the name: ')
if name.isupper():
    print(name)
else:
    print('No')
