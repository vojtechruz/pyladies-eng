# Class Kitten
# Each Kitten has name, can eat and meow

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


kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')
