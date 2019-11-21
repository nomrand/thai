def key(event, plane):
    # "event.keysym" is name of key which you pressed
    # print(event.keysym)

    # Up
    if event.keysym == "Up" or event.keysym == "w" or event.keysym == "8":
        # plane.winfo_y() is current position of y-axis
        # move plane to up side
        plane.place(y=plane.winfo_y() - 5)

    # Down
    if event.keysym == "Down" or event.keysym == "s" or event.keysym == "2":
        # move plane to down side
        plane.place(y=plane.winfo_y() + 5)

    # Left
    if event.keysym == "Left" or event.keysym == "a" or event.keysym == "4":
        # plane.winfo_x() is current position of x
        # move plane to left side
        plane.place(x=plane.winfo_x() - 5)

    # Right
    if event.keysym == "Right" or event.keysym == "d" or event.keysym == "6":
        # move plane to right side
        plane.place(x=plane.winfo_x() + 5)
