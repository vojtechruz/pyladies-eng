import pyglet
from pyglet import gl


def render():
    """Render(draw) state of the game"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # clear the window (paint the window black)
    gl.glColor3f(1, 1, 1)  # set the paint to white
    draw_ball()
    draw_bats()
    draw_net()


def draw_rectangle(x1, y1, x2, y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # draw connected triangles
    gl.glVertex2f(int(x1), int(y1))  # coordinate A
    gl.glVertex2f(int(x1), int(y2))  # coordinate B
    gl.glVertex2f(int(x2), int(y2))  # coordinate C, draw triangle ABC
    gl.glVertex2f(int(x2), int(y1))  # coordinate D, draw triangle BCD
    gl.glEnd()  # stop drawing the triangles


def draw_text(text, x, y, x_position):
    """Draw given text on the given coordinates

    Argument `x_position` can be "left" or "right" - sets where the text will be aligned
    """
    write = pyglet.text.Label(
        text,
        font_name='League Gothic',
        font_size=FONT_SIZE,
        x=x, y=y, anchor_x=x_position)
    write.draw()


def draw_ball():
    draw_rectangle(
    ball_coordinates[0] - BALL_SIZE // 2,
    ball_coordinates[1] - BALL_SIZE // 2,
    ball_coordinates[0] + BALL_SIZE // 2,
    ball_coordinates[1] + BALL_SIZE // 2)


def draw_bats():
    # bats - we will create list of bats coordinates and for each pair of coordinates
    # in this list we will draw the bat
    for x, y in [(0, bat_coordinates[0]), (WINDOW_WIDTH, bat_coordinates[1])]:
        draw_rectangle(
            x - BAT_THICKNESS,
            y - BAT_LENGTH // 2,
            x + BAT_THICKNESS,
            y + BAT_LENGTH // 2)

def draw_net():
    # midfield line (as net) - composed from couple of small rectangles
    for y in range(NET_LENGTH // 2, WINDOW_HEIGHT, NET_LENGTH * 2):
        draw_rectangle(
            WINDOW_WIDTH // 2 - 1,
            y,
            WINDOW_WIDTH // 2 + 1,
            y + NET_LENGTH)


# Window size (in pixels)
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

BALL_SIZE = 20
BAT_THICKNESS = 10
BAT_LENGTH = 100
NET_LENGTH = 20
FONT_SIZE = 42


ball_coordinates = [0, 0]
bat_coordinates = [WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2]  # vertical position of two bats


window = pyglet.window.Window()
window.push_handlers(
    on_draw=render,  # for drawing into the window use function `render`
)
window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.app.run()
