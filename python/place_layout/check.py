def check_position(plane, nglist):

    # Loop all NG boxes, by list
    for ng in nglist:
        x_distance = abs((plane.winfo_x()+50/2) - (ng.winfo_x()+20/2))
        y_distance = abs((plane.winfo_y()+50/2) - (ng.winfo_y()+20/2))

        # Check if the plane is near to ng1
        if x_distance < 50/2 and y_distance < 50/2:
            # if plane is near to ng1, 2, 3
            # return -1 (=game over)
            return -1

    # Check Game Clear
    if plane.winfo_y() < 0:
        # if plane touches goal
        # return 1 (=game clear)
        return 1

    # if plane don't touch any thing
    # return 0 (=nothing happen)
    return 0
