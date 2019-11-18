def key(event, player):
    # Up
    if event.keysym == "Up" or event.keysym == "w" or event.keysym == "8":
        player.place(y=player.winfo_y() - 5)

    # Down
    if event.keysym == "Down" or event.keysym == "s" or event.keysym == "2":
        player.place(y=player.winfo_y() + 5)

    # Left
    if event.keysym == "Left" or event.keysym == "a" or event.keysym == "4":
        player.place(x=player.winfo_x() - 5)

    # Right
    if event.keysym == "Right" or event.keysym == "d" or event.keysym == "6":
        player.place(x=player.winfo_x() + 5)
