# Tride Kotatko jsme nyni pridali konstruktor - __init__(self, jmeno).
# V kontstruktoru nastavujeme hodnotu atributu 'jmeno' z parametru 'jmeno' predaneho do konstruktoru.
# Puvodni zpusob nastavovani atributu z minuleho prikladu je zakomentovan.

# Lets add __init__ method.
# This is special method called initializer, which is called every time a new
# instance is created using Kitty().
#
# We can use it to initialize state of the class, validate inputs etc.

class Kitten:
    def __init__(self, name):
        print(f'Creating kitten with name {name}')
        self.name = name

    def meow(self, message):
        print(f'{self.name}: {message}')


kitty = Kitten('Whiskers')
# kitty.name = 'Whiskers' - we no longer need this, name is passed on line above
kitty.meow('Meow?')
kitty.meow('Time to have a nap.')

another_kitty = Kitten('Fluffy')
# another_kitty.name = 'Fluffy' - we no longer need this, name is passed on line above
another_kitty.meow('Purrrrr.')
