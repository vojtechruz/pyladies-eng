# Added class GourmandKitten which inherits from Kitten
# It has eat() method which already is in Animal parent (inherited by Kitten and then GourmandKitten)
# By defining method with the same name it overrides behavior of the original method
# By calling eat() on GourmandKitten it is calling implementation from that class and not
# from Animal parent
# Puppy does not define eat() method so it still uses the one from Animal



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

class GourmandKitten(Kitten):
    def __str__(self):
        return 'Gourmand Kitten {}'.format(self.name)

    def eat(self, food):
        print('{}: Yuck! I dont like {} at all. I prefer venison.'.format(self.name, food))



kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

gourmandKitty = GourmandKitten('Reginald')
gourmandKitty.meow('I want something delicious!')
gourmandKitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')

