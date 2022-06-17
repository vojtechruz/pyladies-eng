# Added class GourmandKitten which inherits from Kitten
# It has eat() method which already is in Animal parent (inherited by Kitten and then GourmandKitten)
# By defining method with the same name it overrides behavior of the original method
# By calling eat() on GourmandKitten it is calling implementation from that class and not
# from Animal parent
# Puppy does not define eat() method so it still uses the one from Animal



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



kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

gourmandKitty = GourmandKitten('Reginald')
gourmandKitty.meow('I want something delicious!')
gourmandKitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')

