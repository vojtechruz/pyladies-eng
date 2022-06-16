# Class Kitten
# Each Kitten has name, can eat and meow

class Kitten:
    def __init__(self, name):
        print('Creating Kitten with name {}'.format(name))
        self.name = name

    def __str__(self):
        return 'Kitten {}'.format(self.name)

    def eat(self, food):
        print('{}: Yum! {} tastes good.'.format(self.name, food))

    def meow(self, message):
        print('{}: {}'.format(self.name, message))


kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')
