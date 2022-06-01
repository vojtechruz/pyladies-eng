phonebook = {
    'Alice': '603888921',
    'Bob':'777891776',
    'Cecilia':'602345666',
    'Daniel':'728910000',
    'Eve':'777633798',
    'Frank':'608915433',
}

# We can use standard FOR cycle to iterate through a dictionary.
# In such case we iterate through keys
print('Iterating keys with standard FOR cycle')
for key in phonebook:
    print(key)

# Same thing can be achieved by calling dictionary.keys()
print('Iterating keys with phonebook.keys()')
for key in phonebook.keys():
    print(key)

# For iterating values only we can use dictionary.values()
print('Iterating values only with phonebook.values()')
for value in phonebook.values():
    print(value)

# If we need both we can use items(), which returns pairs (key, value)
print('Iterating key/value pairs with phonebook.items()')
for key, value in phonebook.items():
    print("[{}] = {}".format(key, value))


# We cannot remove items during iteration
for key in phonebook.keys():
   del phonebook[key]

# If you want to remove items during iteration you need a workaround
# For example, convert keys to new list and iterate that one
for key in list(phonebook.keys()):
    if key == 'Frank':
        del phonebook[key]

# Let's verify that Frank is really deleted
print('Phonebook without Frank:')
print(phonebook)

# But we can change values when iterating keys
for key in phonebook.keys():
    phonebook[key] = 'something completely different'

print('Phonebook with modified items:')
print(phonebook)