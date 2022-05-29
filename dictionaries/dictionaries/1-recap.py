# Recap - lists
# Collection of items preserving order
colors = ['Red', 'Green', 'Blue']

# We can add items
colors.append('Yellow')

# Or remove them
colors.remove('Blue')

# Function len() gives us number of items in the list
print (len(colors))
print (colors)

# Accessing items with index, starting at 0!
print ('Third items in the list is {}'.format(colors[2]))


# Recap - tuples
# Ordered collection of items
tuple_name_age = ('JC', 33)
print(tuple_name_age)
# Can access with index starting at 0 like with lists
print ('Second item of tuple is {}'.format(tuple_name_age[1]))
# Cannot be changed!


# Both tuples and lists can have items of different types in the same list/tuple
list = [1, 'Purple', False]
tuple = (1, 'Purple', False)