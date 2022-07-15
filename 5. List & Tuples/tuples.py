# To create tuples

tupl = (10,)
tupl = ('Anurag',)

print(tupl)
print(type(tupl))


tup3 = 1, 2, 3, 4, 5, 6
tup3 = 'Anurag', 'Shrishti' , 'Aman'
print(tup3)
print(type(tup3))

lst = [10, 20, 30]
print(lst)
print(type(lst))
tupL = tuple(lst)
print(type(tupL))
print(tupL)


# Indexing and slicing for tuples
tup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 'Anurag', 'Python', 'HTML')
print(tup[9])
print(tup[9:])
print(tup[-1])


# Basic functions for tuple
tup = (90, 20, 30, 40, 50, 60, 70, 80, 10)
print(len(tup))
print(min(tup))
print(max(tup))
print(tup.count(90))
print(tup.index(90))
print(sorted(tup))


# Nested tuple
tup = (50, 60, 74, 85, 94, 785, 265, 487, 523, (168, 61864, 6, 6884, 654, (64, 917, 7891)))
print(tup)
