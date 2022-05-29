# Collection of items of the same type where we lookup values by key
# Eg:
    # Phonebook - find phone number by name
    # Find price by product's name
    #...
phonebook = {
    'Alice': '603888921',
    'Bob':'777891776',
    'Cecilia':'602345666',
    'Daniel':'728910000',
    'Eve':'777633798',
    'Frank':'608915433',
}

# How to find Eve's phone number?
print("Eve's number is {}".format(phonebook['Eve']))