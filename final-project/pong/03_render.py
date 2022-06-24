import pyglet
from pyglet import gl


def render():
    """Render(draw) state of the game"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # clear the window (paint the window black)
    gl.glColor3f(1, 1, 1)  # set the paint to white


def draw_rectangle(x1, y1, x2, y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # draw connected triangles
    gl.glVertex2f(int(x1), int(y1))  # coordinate A
    gl.glVertex2f(int(x1), int(y2))  # coordinate B
    gl.glVertex2f(int(x2), int(y2))  # coordinate C, draw triangle ABC
    gl.glVertex2f(int(x2), int(y1))  # coordinate D, draw triangle BCD
    gl.glEnd()  # stop drawing the triangles


# Window size (in pixels)
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

window = pyglet.window.Window()
window.push_handlers(
    on_draw=render,  # for drawing into the window use function `render`
)
window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.app.run()
