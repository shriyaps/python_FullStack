# List methods

num = [5106, 5160516, 60564, 651809, 65160, 'start', 682, 3242668126, 816, 66810, 681, 351, 601, 3242668126, 1531, 651, 'start']


# list.index()
# To find the first occurance of 3242668126
first_occur = num.index('start')
print('First occurence: ', first_occur)

# list.append()
# To add a new element at the end of the list
new = [0, 1, 2, 3, 4]
print(new)
new.append(5)
print(new)

# list.insert(i, x)     i = index, x = value
# To add a particular value to a particular index
new = [0, 1, 2, 3, 4]
print(new)
new.insert(2, 'Start')
print('After insertion: ', new)

# list.copy()
# To copy all the list elements into a new list and return it
latest = new.copy()
print('The latest list: ', latest)

# list.extend()
# To extend the existing list with another list
a = [0, 1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9, 10]
a.extend(b)
print('Extended list: ', a)

# list.count(value)
# To count the number of occurance
a = [0, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15]
print(a.count(1))

# list.pop()
# To remove the elements from last we use pop()
a = [634284, 64318416, 36184362, 41, 631, 4, 55.3]
print(a)
print(a.pop())
print(a)

# list.sort()
# To sort elements of the list in ascending order
print(a)
a.sort()
print(a)

# list.reverse()
# It will reverse the list
a.reverse()
print(a)

# list.clear()
# Deletes all the elements from the list
a.clear()
print(a)
