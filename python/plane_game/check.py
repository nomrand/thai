def check_position(plane, nglist):

    # Loop all NG boxes, by using list
    # ทำซ้ำสำหรับ กล่องNG โดยใช้ลิสต์
    for ng in nglist:
        x_distance = abs((plane.winfo_x()+50/2) - (ng.winfo_x()+20/2))
        y_distance = abs((plane.winfo_y()+50/2) - (ng.winfo_y()+20/2))

        # Check if the plane is close to NG box
        # ตรวจสอบว่า เครื่องบินอยู่ใกล้กับ กล่องNG หรือไม่
        if x_distance < 50/2 and y_distance < 50/2:
            # if plane is close to NG box, return value is -1 (=lose the game)
            # ถ้าเครื่องบินอยู่ใกล้กับ กล่องNG  ส่งคืนค่า -1 (=แพ้เกม)
            return -1

    # Check whether win the game
    # ตรวจสอบว่าชนะเกม
    if plane.winfo_y() < 0:
        # if plane touches goal, return value is 1 (=win the game)
        # ถ้าเครื่องบินแตะต้องเป้าหมาย  ส่งคืนค่า 1 (=ชนะเกม)
        return 1

    # if plane didn't touch anything, return value is 0
    # ถ้าเครื่องบินไม่ได้แตะต้องอะไรเลย ส่งคืนค่า 0
    return 0
