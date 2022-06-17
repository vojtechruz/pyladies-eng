# So far it is difficult to tell kittens apart when they meow.
# Lets print the kitten's name along with the message when they meow.
#
# How can we access the name of the current kitten though?
# We can actually use 'self' parameter of the meow method, which points
# to the current instance of the kitten class.
# self.name gives us the name of the kitten which is currently meowing
#
# Self needs to be first parameter of each class method
# But only in method definition. When we call method we dont pass in 'self',
# python does that for us


class Kitten:
    def meow(self, message):
        print('{}: {}'.format(self.name, message))


kitty = Kitten()
kitty.name = 'Whiskers'
kitty.meow('Meow?')
kitty.meow('Time to have a nap.')

another_kitty = Kitten()
another_kitty.name = 'Fluffy'
another_kitty.meow('Purrrrr.')
