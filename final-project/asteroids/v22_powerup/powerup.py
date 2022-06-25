from space_object import SpaceObject
import math
POWERUP_LIFETIME = 10
class Powerup(SpaceObject):
    def __init__(self, batch, objects, window):
        super().__init__(batch, objects, window)
        self.can_collide = True
        self.rotation = math.radians(90)
        self.lifetime_remaining = POWERUP_LIFETIME

    def image_path(self):
        return "../assets/PNG/Power-ups/powerupBlue_shield.png"

    def tick(self, time_elapsed, keys_pressed, window):
        super().update_sprite()

        self.lifetime_remaining = self.lifetime_remaining - time_elapsed
        if self.lifetime_remaining <= 0:
            self.destroy_object()

    def apply_powerup(self):
        self.objects[0].shield_active = True