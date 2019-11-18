def check_position(player, ng1, ng2, ng3):
    # Check whether player is near ng1
    if abs(player.winfo_x()+50/2 - ng1.winfo_x()) < 50/2:
        if abs(player.winfo_y()+50/2 - ng1.winfo_y()) < 50/2:
            return -1

    # Check whether player is near ng2
    if abs(player.winfo_x()+50/2 - ng2.winfo_x()) < 50/2:
        if abs(player.winfo_y()+50/2 - ng2.winfo_y()) < 50/2:
            return -1

    # Check whether player is near ng3
    if abs(player.winfo_x()+50/2 - ng3.winfo_x()) < 50/2:
        if abs(player.winfo_y()+50/2 - ng3.winfo_y()) < 50/2:
            return -1

    # Check Game Clear
    if player.winfo_y() < 0:
        return 1

    return 0
