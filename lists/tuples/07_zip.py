animals = 'dog', 'cat', 'fox', 'badger'
attributes = 'loyal', 'lazy', 'cunning', 'furious'

for pair in zip(animals, attributes):
    print(pair)
    print('{} is {}'.format(pair[0], pair[1]))

# for person, attribute in zip(animals, attributes):
#     print('{} is {}'.format(person, attribute))
