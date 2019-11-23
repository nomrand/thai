# This line is needed to use GUI
# ↓ บรรทัดนี้จำเป็นต้องใช้ GUI
from tkinter import *
import random


# This is main part of program

# These 2 lines are making screen outline.
# These are necessary for GUI program.
# 2 บรรทัดเหล่านี้กำลังสร้างเค้าโครงหน้าต่าง GUI
# สิ่งเหล่านี้จำเป็นสำหรับโปรแกรม GUI
root = Tk(className='shooting star simulator ver.1')
root.geometry("400x400")  # ความกว้าง=400 ความสูง=400


# ##########################
# ###  Create GUI Parts  ###
# ##########################
# สร้าง label
label_shooting_star = Label(root, text="★")
random_y = random.randint(0, 200)
label_shooting_star.place(x=0, y=random_y)


# ##########################
# ###  Create GUI Parts  ###
# ##########################
def move():
    position = (label_shooting_star.winfo_x() + 3,
                label_shooting_star.winfo_y() + 3)
    label_shooting_star.place(x=position[0], y=position[1])

    if position[0] > 400 or position[1] > 400:
        random_y = random.randint(0, 200)
        label_shooting_star.place(x=0, y=random_y)

    root.after(10, move)


move()

# This is an also necessary line for GUI program.
# (This line must be placed at the end of GUI program)
# นี่เป็นบรรทัดที่จำเป็นสำหรับโปรแกรม GUI
# (บรรทัดนี้ควรอยู่ที่ท้ายโปรแกรม GUI)
root.mainloop()
