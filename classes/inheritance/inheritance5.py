# GourmandKitten now meows differently that ordinary Kitten
# With super() we can call methods on the parent class, in this case
# it is the direct parent - Animal
# We can pass method inputs to parent as well.
# Here we take the original message and we add "I would like to eat something delicious"

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

class GourmandKitten(Kitten):
    def __str__(self):
        return f'Gourmand Kitten {self.name}'

    def eat(self, food):
        print(f'{self.name}: Yuck! I dont like {food} at all. I prefer venison.')

    def meow(self, zprava):
        super().meow(f"{zprava} I would like to eat something delicious.")



kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

gourmandKitty = GourmandKitten('Reginald')
gourmandKitty.meow('Meow?!')
gourmandKitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')
