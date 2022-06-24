import pyglet
from pyglet import gl
from pyglet.window import key
import random


def render():
    """Render(draw) state of the game"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # clear the window (paint the window black)
    gl.glColor3f(1, 1, 1)  # set the paint to white
    background.blit_tiled(0, 0, 0, window.width, window.height)
    draw_ball()
    draw_net()
    draw_bats()
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
    gl.glColor3f(1, 0, 0)  # set the paint to red

    draw_rectangle(
      ball_coordinates[0] - BALL_SIZE // 2,
      ball_coordinates[1] - BALL_SIZE // 2,
      ball_coordinates[0] + BALL_SIZE // 2,
      ball_coordinates[1] + BALL_SIZE // 2)


def draw_bats():
    # bats - we will create list of bats coordinates and for each pair of coordinates
    # in this list we will draw the bat
    for x, y, color in [(0, bat_coordinates[0], player_colors[0]), (WINDOW_WIDTH, bat_coordinates[1], player_colors[1])]:
        red, green, blue = color
        gl.glColor3f(red, green, blue)

        draw_rectangle(
            x - BAT_THICKNESS,
            y - BAT_LENGTH // 2,
            x + BAT_THICKNESS,
            y + BAT_LENGTH // 2)


def draw_net():
    gl.glColor3f(1, 0, 0)  # set the paint to red

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


def revive(dt):
    ball_coordinates[0] += ball_speed[0] * dt
    ball_coordinates[1] += ball_speed[1] * dt

    bounce_walls()
    bounce_bats()
    move_bats(dt)


def bounce_bats():
    bat_min = ball_coordinates[1] - BALL_SIZE/2 - BAT_LENGTH/2
    bat_max = ball_coordinates[1] + BALL_SIZE/2 + BAT_LENGTH/2

    # bounce to the left
    if ball_coordinates[0] < BAT_THICKNESS + BALL_SIZE / 2:
        if bat_min < bat_coordinates[0] < bat_max:
            # bat is at the right spot we can bounce the ball back
            ball_speed[0] = abs(ball_speed[0])
        else:
            # bat is not at the right place the player lost
            score[1] += 1
            reset()

    # bounce to the right
    if ball_coordinates[0] > WINDOW_WIDTH - (BAT_THICKNESS + BALL_SIZE / 2):
        if bat_min < bat_coordinates[1] < bat_max:
            ball_speed[0] = -abs(ball_speed[0])
        else:
            score[0] += 1
            reset()


def bounce_walls():
    if ball_coordinates[1] < BALL_SIZE // 2:
        ball_speed[1] = abs(ball_speed[1])

    if ball_coordinates[1] > WINDOW_HEIGHT - BALL_SIZE // 2:
        ball_speed[1] = -abs(ball_speed[1])


def move_bats(dt):
    for bat_number in (0, 1):
        # movement according to pressed keys (function `key_press`)
        if ('up', bat_number) in keys_pressed:
            bat_coordinates[bat_number] += BAT_SPEED * dt
        if ('down', bat_number) in keys_pressed:
            bat_coordinates[bat_number] -= BAT_SPEED * dt

        # bottom stop - when bat is down bellow we will set it to the minimum
        if bat_coordinates[bat_number] < BAT_LENGTH / 2:
            bat_coordinates[bat_number] = BAT_LENGTH / 2
        # top stop - when bat is too high we will set it to the maximum
        if bat_coordinates[bat_number] > WINDOW_HEIGHT - BAT_LENGTH / 2:
            bat_coordinates[bat_number] = WINDOW_HEIGHT - BAT_LENGTH / 2


def reset():
    ball_coordinates[0] = WINDOW_WIDTH // 2
    ball_coordinates[1] = WINDOW_HEIGHT // 2

    # x speed - right or left
    if random.randint(0, 1):
        ball_speed[0] = SPEED
    else:
        ball_speed[0] = -SPEED
    # y speed - completely random
    ball_speed[1] = random.uniform(-1, 1) * SPEED


# Window size (in pixels)
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

BALL_SIZE = 20
BAT_THICKNESS = 10
BAT_LENGTH = 100
NET_LENGTH = 20
FONT_SIZE = 42
TEXT_ALIGN = 30

SPEED = 200  # pixels per second
BAT_SPEED = SPEED * 1.5  # also pixels per second

ball_coordinates = [0, 0]
bat_coordinates = [WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2]  # vertical position of two bats
score = [0, 0]  # score for 2 players
keys_pressed = set()  # set of pressed keys
ball_speed = [0, 0]  # x, y components of ball speed -- set in reset()
player_colors = [(0, 1, 0), (0, 0, 1)]


image = pyglet.image.load('background.png')
background = pyglet.image.TileableTexture.create_for_image(image)

reset()
window = pyglet.window.Window()
window.push_handlers(
    on_draw=render,  # for drawing into the window use function `render`
    on_key_press=key_press,  # when key is pressed call function `key_press`
    on_key_release=key_release,  # when key is released call `key_release`
)
window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.clock.schedule(revive)
pyglet.app.run()
