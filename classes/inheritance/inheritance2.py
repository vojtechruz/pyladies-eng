# Now let us create class Puppy
# Puppy is similiar to Kitten in some cases and different in others. Both can eat.
# Method eat is duplicated in both classes.

class Kitten:
    def __init__(self, name):
        print(f'Creating Kitten with name {name}')
        self.name = name

    def __str__(self):
        return f'Kitten {self.name}'

    def eat(self, food):
        print(f'{self.name}: Yum! {food} tastes good.')

    def meow(self, message):
        print(f'{self.name}: {message}')

class Puppy:
    def __init__(self, name):
        print(f'Creating Puppy with name {name}')
        self.name = name

    def __str__(self):
        return f'Puppy {self.name}'

    def eat(self, food):
        print(f'{self.name}: Yum! {food} tastes good.')

    def bark(self, message):
        print(f'{self.name}: Bark! {message}')


kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')
