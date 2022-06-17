# Class Kitten stays the same as in the previous example
# Now let's create two instances of the Kitten class.
# These are just two different cats created from the same blueprint (Class).
#    kitty = Kitten()
#    another_kitty = Kitten()
#
# To tell our kittens apart, lets assign them names into class attribute 'name'
#    kitty.name = 'Whiskers'
#    another_kitty.name = 'Fluffy'
#
# Now we can access the name later and print it to the console.
#    print('Name of first kitty is {}'.format(kitty.name))
#    print('Name of second kitty is {}'.format(another_kitty.name))


class Kitten:
    def meow(self, message):
        print('Kitten: {}'.format(message))


kitty = Kitten()
kitty.name = 'Whiskers'
print('Name of first kitty is {}'.format(kitty.name))

another_kitty = Kitten()
another_kitty.name = 'Fluffy'
print('Name of second kitty is {}'.format(another_kitty.name))
