import pyglet
from pyglet import gl
from pyglet.window import key

def render():
    """Render(draw) state of the game"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # clear the window (paint the window black)
    gl.glColor3f(1, 1, 1)  # set the paint to white
    draw_ball()
    draw_bats()
    draw_net()
    draw_score()


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


def draw_score():
    draw_text(str(score[0]),
              x=TEXT_ALIGN,
              y=WINDOW_HEIGHT - TEXT_ALIGN - FONT_SIZE,
              x_position='left')

    draw_text(str(score[1]),
              x=WINDOW_WIDTH - TEXT_ALIGN,
              y=WINDOW_HEIGHT - TEXT_ALIGN - FONT_SIZE,
              x_position='right')


def key_press(symbol, modifiers):
    if symbol == key.W:
        keys_pressed.add(('up', 0))
    if symbol == key.S:
        keys_pressed.add(('down', 0))
    if symbol == key.UP:
        keys_pressed.add(('up', 1))
    if symbol == key.DOWN:
        keys_pressed.add(('down', 1))


def key_release(symbol, modifiers):
    if symbol == key.W:
        keys_pressed.discard(('up', 0))
    if symbol == key.S:
        keys_pressed.discard(('down', 0))
    if symbol == key.UP:
        keys_pressed.discard(('up', 1))
    if symbol == key.DOWN:
        keys_pressed.discard(('down', 1))


# Window size (in pixels)
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

BALL_SIZE = 20
BAT_THICKNESS = 10
BAT_LENGTH = 100
NET_LENGTH = 20
FONT_SIZE = 42
TEXT_ALIGN = 30

ball_coordinates = [0, 0]
bat_coordinates = [WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2]  # vertical position of two bats
score = [0, 0]  # score for 2 players
keys_pressed = set()  # set of pressed keys

window = pyglet.window.Window()
window.push_handlers(
    on_draw=render,  # for drawing into the window use function `render`
    on_key_press=key_press,  # when key is pressed call function `key_press`
    on_key_release=key_release,  # when key is released call `key_release`
)
window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.app.run()
