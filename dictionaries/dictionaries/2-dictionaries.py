# Dictionary - Contains key/value pairs
    #Eg.
    # Name -> 'Jane'
    # Age -> 30
    # FavoriteColor -> 'Blue'

person = {
    'Name': 'Jane',
    'Age': 30,
    'FavoriteColor': 'Blue'
}

print(person)

# Items are not accessed by numeric index but by KEY
print('Name of the person is  {}'.format(person['Name']))
print('Age of the person is {}'.format(person['Age']))
print('Favorite color of the person is {}'.format(person['FavoriteColor']))

# Accessing non-existing key results in KeyError
print('Eye color of the person is {}'.format(person['EyeColor']))

# We can add new items (if the KEY is already present, it will overwrite the value)
person['EyeColor'] = 'Green'

# Or remove items
del person['Age']
print(person)