class Cat:
    def __init__(self):         # No need to pass in number of lives, cats are born always with 9
        self.number_of_lives = 9

    def meow(self):
        print("Meow!")

    def is_alive(self):
        return self.number_of_lives > 0

    def take_life(self):
        if self.is_alive():
            print("Ouch!")
            self.number_of_lives -= 1
            print(f"Cat now has {self.number_of_lives} lives")
        else:
            print("The poor cat is already dead!")

    def eat(self, food):
        if not self.is_alive():
            print("No point in feeding a dead cat!")
        elif food == "fish" and self.number_of_lives < 9:
            self.number_of_lives += 1
            print(f"The cat ate the fish and restored one life. It now has {self.number_of_lives} lives.")
        else:
            print(f"The cat ate {food}.")

    def __str__(self):
        if not self.is_alive():
            return "ex-Cat"

        return f"Cat, number of lives: {self.number_of_lives}"


cat = Cat()
cat.meow()
cat.take_life()
cat.eat("mouse")
cat.eat("fish")
print(cat)
