# GourmandKitten now meows differently that ordinary Kitten
# With super() we can call methods on the parent class, in this case
# it is the direct parent - Animal
# We can pass method inputs to parent as well.
# Here we take the original message and we add "I would like to eat something delicious"

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

    def meow(self, zprava):
        super().meow("{} I would like to eat something delicious.".format(zprava))



kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.eat('Mouse')

gourmandKitty = GourmandKitten('Reginald')
gourmandKitty.meow('Meow?!')
gourmandKitty.eat('Mouse')

puppy = Puppy('Rex')
puppy.bark('I didnt chew these shoes!')
puppy.eat('Bone')
