import pyglet
from spaceship import Spaceship
from asteroid import Asteroid
from pyglet import gl
import random
from explosion import Explosion
from powerup import Powerup

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
ASTEROID_COUNT = 4
MAX_ASTEROID_COUNT = 20
ASTEROID_MIN_SPEED = 10
ASTEROID_MAX_SPEED = 50
ASTEROID_SPAWN_CHANCE = 5

objects = []
keys_pressed = set()
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
game_over = False
batch = pyglet.graphics.Batch()
background_image = pyglet.image.load('../assets/Backgrounds/darkPurple.png')
background = pyglet.image.TileableTexture.create_for_image(background_image)

def init_spaceship():
    spaceship = Spaceship(batch, objects, window)
    spaceship.x = window.width/2
    spaceship.y = window.height/2

def init_asteroids():
    for i in range(ASTEROID_COUNT):
        spawn_asteroid()

def spawn_asteroid():
    asteroid = Asteroid(batch, objects, window)
    position = random.choice([0, 1])
    if position == 0:
        asteroid.x = random.randint(0, window.width)
        asteroid.y = random.choice([0, window.height])
    else:
        asteroid.x = random.choice([0, window.width])
        asteroid.y = random.randint(0, window.height)

    asteroid.x_speed = random.choice([-1, 1]) * random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
    asteroid.y_speed = random.choice([-1, 1]) * random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)


def draw_all_objects():
    window.clear()

    background.blit_tiled(0, 0, 0, window.width, window.height)

    if(game_over):
        game_over_label = pyglet.text.Label(
            'Game Over',
            font_name='League Gothic',
            font_size=40,
            x=window.width / 2,
            y=window.height / 2,
            anchor_x='center')
        game_over_label.draw()


    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()

def collision(obj):
    target_alive = obj.hit()
    if not target_alive:
        obj.destroy_object()
        explosion_target = Explosion(obj.batch, obj.objects, obj.window)
        explosion_target.x = obj.x
        explosion_target.y = obj.y

    ship_alive = objects[0].hit()
    if ship_alive:
        return

    objects[0].destroy_object()
    batch.draw()

    global game_over
    game_over = True

    pyglet.clock.unschedule(tick_all_objects)

def tick_all_objects(time_elapsed):
    ship = objects[0]

    for obj in objects:
        obj.tick(time_elapsed, keys_pressed, window)

        if isinstance(obj, Powerup) and obj.overlaps(ship):
            obj.destroy_object()
            obj.apply_powerup()
            break

        # Check all object if they collide with ship
        if(obj.can_collide and obj.overlaps(ship)):
            collision(obj)

    random_number = random.randint(0,100)
    if(random_number < ASTEROID_SPAWN_CHANCE
    and get_asteroid_count() < MAX_ASTEROID_COUNT):
        spawn_asteroid()

def get_asteroid_count():
    count = 0
    for object in objects:
        if isinstance(object, Asteroid):
            count = count + 1
    print(count)
    return count


def on_key_pressed(key, modifiers):
    keys_pressed.add(key)

def on_key_released(key, modifiers):
    keys_pressed.remove(key)


init_spaceship()
init_asteroids()
window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
)
pyglet.clock.schedule_interval(tick_all_objects, 1/30)
# window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.app.run()