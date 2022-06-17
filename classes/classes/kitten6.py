# Kitten class stays the same as before
# Lets try to print our Kitten instances to the console
# The result is not what we would expect

class Kitten:
    def __init__(self, name):
        print(f'Creating kitten with name {name}')
        self.name = name

    def meow(self, message):
        print(f'{self.name}: {message}')


kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.meow('Time to have a nap.')

another_kitty = Kitten('Fluffy')
another_kitty.meow('Purrrrr.')

print(kitty)
print(another_kitty)
