# New class Animal
# Kitten and Puppy inherit from Animal
# Method eat() was moved to the animal from Kitten and Puppy, their common ancestor
# We can still call eat() on both Kitten and Puppy but it is taken from the ancestor Animal class


class Animal:
    def __init__(self, name):
        print(f'Creating animal {name}')
        self.name = name

    def eat(self, food):
        print(f'{self.name}: Yum! {food} tastes good.')


class Kitten(Animal):
    def __str__(self):
        return f'Kitten {self.name}'

    def meow(self, message):
        print(f'{self.name}: {message}')


class Puppy(Animal):

    def __str__(self):
        return f'Puppy {self.name}'

    def bark(self, message):
        print(f'{self.name}: Bark! {message}')



kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')

