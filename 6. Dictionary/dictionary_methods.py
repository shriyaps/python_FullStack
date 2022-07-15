# Dictionary methods
detail = {'Name':'Anurag',
          'Location':'Thane',
          'Mobile':9892631384,
          'Coding':'Python'}

# dict.values() to get all the values from the dictionary
a = list(detail.values())
print(a)
print(type(detail.values()))


## dict.keys() to get all the keys from the dictionary
      
      
a = list(detail.keys())
print(a)
print(type(detail.keys))
a = list(detail.keys())
print(a)
print(type(detail.keys()))

# dict.update() to add a new key-value pairs to the dictionary
detail.update({'Surname':'Chiplunkar'})
print(detail)

# dict.setdefault() returns a value of the specified key,
# if the key is not present
# Insert the key with the specified value
detail.setdefault('Company', 'Freelancer')
print(detail)

# dict.popitem() removes the last inserted key-value pair
detail.popitem()
print(detail)

# dict.pop() removes the element with the specified key
detail.pop('Surname')
detail.pop('Mobile')
print(detail)

# dicts.items() returns a list containing a tuple for each key value pair
a = detail.items()
print(a)
      
# dict.fromkeys(sequence, default_value) returns a dictionary
# with the specified keys and specified value
tup = ('Name', 'Surname', 'Age', 'Company', 'Location')
values = 'Default'
detail = detail.fromkeys(tup, values)
print(detail)

# dict.copy() returns a copy of the dictionary
duplicate = detail.copy()
print("Identity of detail: ", id(detail))
print(detail)

print()
print('Identity of duplicate: ', id(duplicate))
print(duplicate)

# dict.get(key, message) returns the value for the given key
a = detail.get('Name', 'No such key present')
print(a)

# To find length of dictionary
print("The length of the dictionary is: ", len(detail))
print(detail)

# dict.clear() this will remove all the elements from the dictionary
detail.clear()
print(detail)

