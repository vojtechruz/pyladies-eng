# Now let us create class Puppy
# Puppy is similiar to Kitten in some cases and different in others. Both can eat.
# Method eat is duplicated in both classes.

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

class Puppy:
    def __init__(self, name):
        print('Creating Puppy with name {}'.format(name))
        self.name = name

    def __str__(self):
        return 'Puppy {}'.format(self.name)

    def eat(self, food):
        print('{}: Yum! {} tastes good.'.format(self.name, food))

    def bark(self, message):
        print('{}: Bark! {}'.format(self.name, message))


kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')
