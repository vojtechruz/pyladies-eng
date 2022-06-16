# Extended version of Kitten.
# We can now pass what message should the cat say

class Kitten:
    def meow(self, message):
        print('Kitten: {}'.format(message))


kitty = Kitten()
kitty.meow('Meow?')
kitty.meow('MEOOOOOOOOWWW!')
