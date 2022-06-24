# We can exit the window by pressing ESC
import pyglet

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

window = pyglet.window.Window()
window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.app.run()
