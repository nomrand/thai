from tkinter import Tk, Canvas, NW
from random import randint
import os
from PIL import Image, ImageTk
import input
import check

SCREEN_TITLE = "PuyoPuyo"
CANVAS = None
SIZE = 40
COLS = 10
ROWS = 10
# create a 2 dimensional list such as [[0, 0, ...], [0, 0, ...], ...]
CURRENT_MATRIX = [[0 for i in range(ROWS)] for i in range(COLS)]
DEFAULT_POS = (int(COLS/2), 0)
TARGET_POS = DEFAULT_POS
TARGET_IMAGE = 0

SPEED_MS = 500
PUYO_IMAGES = ['', '', '', '']


def start():
    global CANVAS
    root = Tk(className=SCREEN_TITLE)
    root.minsize(SIZE * COLS, SIZE * ROWS)

    # create canvas
    CANVAS = Canvas(root, width=SIZE * COLS, height=SIZE * ROWS)
    CANVAS.pack()
    # canvas event
    CANVAS.bind("<Key>", input.key)
    CANVAS.bind("<1>", input.click)
    CANVAS.focus_set()

    # create images
    PUYO_IMAGES[0] = create_image('img/puyo_green.png')
    PUYO_IMAGES[1] = create_image('img/puyo_red.png')
    PUYO_IMAGES[2] = create_image('img/puyo_blue.png')
    PUYO_IMAGES[3] = create_image('img/puyo_yellow.png')
    global TARGET_IMAGE
    TARGET_IMAGE = randint(1, len(PUYO_IMAGES))

    animation(root)

    # To keep GUI window running
    root.mainloop()


def create_image(path):
    real_path = os.path.join(os.path.dirname(__file__), path)
    img = Image.open(real_path)
    img = img.resize((SIZE, SIZE), Image.ADAPTIVE)
    img = ImageTk.PhotoImage(image=img)
    return img


def animation(r):
    if not check.check(CURRENT_MATRIX):
        # if no images deleted, target(user-controlled) image can fall
        fall_image()

    draw()

    # this function is called after SPEED_MS milli sec passed
    r.after(SPEED_MS, lambda: animation(r))


def draw():
    CANVAS.delete("all")

    # Draw screen as matrix
    for col in range(len(CURRENT_MATRIX)):
        for row in range(len(CURRENT_MATRIX[col])):
            image_type = CURRENT_MATRIX[col][row]

            if image_type == 0:
                # Empty space
                pass
            else:
                # Draw image
                CANVAS.create_image(
                    col * SIZE,
                    row * SIZE,
                    image=PUYO_IMAGES[image_type-1],
                    anchor=NW)

            if (col, row) == TARGET_POS:
                CANVAS.create_image(
                    col * SIZE,
                    row * SIZE,
                    image=PUYO_IMAGES[TARGET_IMAGE-1],
                    anchor=NW)

    CANVAS.update()


def fall_image():
    global TARGET_POS, TARGET_IMAGE
    is_new = False
    if TARGET_POS[1] < ROWS - 1:
        if CURRENT_MATRIX[TARGET_POS[0]][TARGET_POS[1] + 1] != 0:
            CURRENT_MATRIX[TARGET_POS[0]][TARGET_POS[1]] = TARGET_IMAGE
            is_new = True
            TARGET_POS = DEFAULT_POS
            TARGET_IMAGE = randint(1, len(PUYO_IMAGES))
        else:
            TARGET_POS = (TARGET_POS[0], TARGET_POS[1] + 1)
    else:
        CURRENT_MATRIX[TARGET_POS[0]][TARGET_POS[1]] = TARGET_IMAGE
        is_new = True

    if is_new:
        TARGET_POS = DEFAULT_POS
        TARGET_IMAGE = randint(1, len(PUYO_IMAGES))


def right():
    global TARGET_POS
    if TARGET_POS[0] != COLS - 1:
        TARGET_POS = (TARGET_POS[0] + 1, TARGET_POS[1])
        draw()


def left():
    global TARGET_POS
    if TARGET_POS[0] != 0:
        TARGET_POS = (TARGET_POS[0] - 1, TARGET_POS[1])
        draw()


def down():
    if not check.check(CURRENT_MATRIX):
        # if no images deleted, target(user-controlled) image can fall
        fall_image()
    draw()
