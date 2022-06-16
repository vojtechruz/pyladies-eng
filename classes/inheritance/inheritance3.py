# New class Animal
# Kitten and Puppy inherit from Animal
# Method eat() was moved to the animal from Kitten and Puppy, their common ancestor
# We can still call eat() on both Kitten and Puppy but it is taken from the ancestor Animal class


class Animal:
    def __init__(self, name):
        print('Creating animal {}'.format(name))
        self.name = name

    def eat(self, food):
        print('{}: Yum! {} tastes good.'.format(self.name, food))

class Kitten(Animal):
    def __str__(self):
        return 'Kitten {}'.format(self.name)

    def meow(self, message):
        print('{}: {}'.format(self.name, message))

class Puppy(Animal):

    def __str__(self):
        return 'Puppy {}'.format(self.name)

    def bark(self, message):
        print('{}: Bark! {}'.format(self.name, message))



kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')

