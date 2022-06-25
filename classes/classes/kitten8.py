# Lets add __str__ method, which is used when instances need to be converted to string.
# Whatever the method returns is used as string representation of the instance
# So when we call print(kitty) it will cal __str__ method and print its result to the console

class Kitten:
    # This way we can restrict which fields
    # can be assigned
    # They don't have to be assigned a value
    # But we cannot assign fields with any other names
    __slots__ = ('name', 'color')

    def __init__(self, name):
        print(f'Creating kitten with name {name}')
        self.name = name

    def __str__(self):
        return f'Kitten with name {self.name}'

    def meow(self, message):
        print(f'{self.name}: {message}')


kitty = Kitten('Whiskers')
kitty.meow('Meow?')
kitty.meow('Time to have a nap.')

another_kitty = Kitten('Fluffy')
another_kitty.meow('Purrrrr.')

# This is possible as 'color' is allowed via __slots__
another_kitty.color = 'Brown'
# This is not possible as 'age' is not in __slots__
# The application will fail with an error
# AttributeError: 'Kitten' object has no attribute 'age'
another_kitty.age = 7

print(kitty)
print(another_kitty)