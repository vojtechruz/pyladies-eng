import pyglet
import math

# Degrees per second
ROTATION_SPEED = 200
ACCELERATION = 200

class SpaceObject:
    def __init__(self, batch, objects, window):

        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.can_collide = False
        self.shield_active = False
        self.objects = objects
        self.batch = batch
        self.window = window

        shield_path = "../assets/PNG/shield.png"
        shield_image = pyglet.image.load(shield_path)
        shield_image.anchor_x = shield_image.width // 2
        shield_image.anchor_y = shield_image.height // 2
        self.shield_sprite = pyglet.sprite.Sprite(shield_image, batch=batch)
        self.shield_sprite.scale = 2/3
        self.shield_sprite.visible = False

        image = pyglet.image.load(self.image_path())
        # Image is positioned by its middle, not lower left corner
        # Also important for rotation
        # // means integer division (floor) - 5//2 is 2 but 5/2 is 2.5
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        self.radius = self.sprite.width//2 + 3
        objects.append(self)
        self.sprite.visible = False

    def update_sprite(self):
        self.sprite.visible = True
        self.sprite.x = self.x
        self.sprite.y = self.y

        self.shield_sprite.x = self.x
        self.shield_sprite.y = self.y
        self.shield_sprite.visible = self.shield_active
        # we have rotation in rads, pyglet uses degrees
        # also, pyglet's zero is up, ours is on the right, right?
        self.sprite.rotation = 90 - math.degrees(self.rotation)

    def hit(self):
        if self.shield_active:
            self.shield_active = False
            return True

        return False

    def destroy_object(self):
        self.shield_sprite.visible = False
        self.shield_sprite.delete()
        self.sprite.delete()
        self.objects.remove(self)

    def distance(self, a, b, wrap_size):
        """Distance in one direction (x or y)"""
        result = abs(a - b)
        if result > wrap_size / 2:
            result = wrap_size - result
        return result

    def overlaps(self, other):
        """Returns true iff two space objects overlap"""
        distance_squared = (self.distance(self.x, other.x, self.window.width) ** 2 +
                            self.distance(self.y, other.y, self.window.height) ** 2)
        max_distance_squared = (self.radius + other.radius) ** 2

        return distance_squared < max_distance_squared - 1000

    def hit_by_laser(self):
        return False


