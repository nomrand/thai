import screen


def key(event):
    print("pressed", event.keysym)

    # Up
    if event.keysym == "Up" or event.keysym == "w" or event.keysym == "8":
        pass

    # Down
    if event.keysym == "Down" or event.keysym == "s" or event.keysym == "2":
        screen.down()

    # Left
    if event.keysym == "Left" or event.keysym == "a" or event.keysym == "4":
        screen.left()

    # Right
    if event.keysym == "Right" or event.keysym == "d" or event.keysym == "6":
        screen.right()


def click(event):
    print("clicked at", event.x, event.y)
