dict1 = {'name': 'TOM', 'age': 20, 'gender': 'male'}
# keys
for key in dict1.keys():
    print(key)

# values
for value in dict1.values():
    print(value)

# items
for item in dict1.items():
    print(item)
for key, value in dict1.items():
    print(f'{key}:{value}')