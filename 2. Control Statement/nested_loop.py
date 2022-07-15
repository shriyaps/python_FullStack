# Display the star pattern in right angled triangle

# range(start, stop-1, step)

for i in range(1,11):
    for j in range(1,i+1):
        print('*',end = '')
    print()


# Display numbers from 1 to 100 in 10 rows and 10 columns
for x in range(1,11):
#    print("The value of x is: ", x)
    for y in range(1,11):
#        print("The value of y is: ", y)
        print('{}'.format(x*y), end = '\t')
    print()

print('Python', end = ',')
print('Java', end = ',')
print('C++', end = '.')
print('Javascript')
print('HTML')
