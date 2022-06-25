from powerup import Powerup
import random

POWERUP_SPAWN_CHANCE = 10

def try_spawn_random_powerup(batch, objects, window, x, y):
    random_number = random.randint(0, 100)
    print(random_number)
    if random_number > POWERUP_SPAWN_CHANCE:
        return False


    powerup = Powerup(batch, objects, window)
    powerup.x = x
    powerup.y = y

    return True